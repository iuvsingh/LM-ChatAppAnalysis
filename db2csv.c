#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>
#include <csv.h>

int main(int argc, char* argv[]) {
  // Define the list of databases and tables to process
  const char* databases[] = {"database1.db", "database2.db", "database3.db"};
  const char* tables[] = {"table1", "table2", "table3"};

  // Loop over each database and table
  for (int i = 0; i < sizeof(databases) / sizeof(char*); i++) {
    sqlite3* db;
    sqlite3_stmt* stmt;
    int rc;
    const char* query = "SELECT * FROM %s";
    const char* filename = "%s_%s.csv";
    csv_writer writer;
    FILE* fp;

    // Open the database
    rc = sqlite3_open(databases[i], &db);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
      sqlite3_close(db);
      continue;
    }

    // Prepare the SQL query
    char sql[100];
    sprintf(sql, query, tables[i]);
    rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Cannot prepare SQL statement: %s\n", sqlite3_errmsg(db));
      sqlite3_close(db);
      continue;
    }

    // Open the output CSV file
    char output_file[100];
    sprintf(output_file, filename, databases[i], tables[i]);
    fp = fopen(output_file, "w");
    if (fp == NULL) {
      fprintf(stderr, "Cannot open CSV file for writing.\n");
      sqlite3_finalize(stmt);
      sqlite3_close(db);
      continue;
    }

    // Initialize the CSV writer
    csv_init(&writer, 0);

    // Write the CSV header row
    csv_write_cell(&writer, "Column1");
    csv_write_cell(&writer, "Column2");
    csv_write_cell(&writer, "Column3");
    csv_end_row(&writer);

    // Iterate over the result set and write each row to the CSV file
    while (sqlite3_step(stmt) == SQLITE_ROW) {
      csv_write_cell(&writer, (char*)sqlite3_column_text(stmt, 0));
      csv_write_cell(&writer, (char*)sqlite3_column_text(stmt, 1));
      csv_write_cell(&writer, (char*)sqlite3_column_text(stmt, 2));
      csv_end_row(&writer);
    }

    // Flush and close the CSV writer and file
    csv_flush(&writer, fp);
    csv_free(&writer);
    fclose(fp);

    // Clean up
    sqlite3_finalize(stmt);
    sqlite3_close(db);
  }

  return 0;
}

