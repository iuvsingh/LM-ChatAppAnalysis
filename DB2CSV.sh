# #!/bin/bash


# if [ -e /home/kali/Desktop/Imports/Signal/database.sqlite ]; then
# 	sqlite3 database.sqlite <<EOF  #signal
# 	.headers on
# 	.mode csv
# 	.output signalMessagesDB.csv
# 	SELECT * FROM message
# EOF
# fi

# sqlite3 msgstore.db <<EOF # whatsapp
# .headers on
# .mode csv
# .output whatsAppMessagesDB.csv
# SELECT * FROM message
# EOF

#!/bin/bash

# Replace "/path/to/directory" with the absolute path to the directory you want to search
directory="/home/usingh2/Desktop/imports"

# Recursively search for all .db and .sqlite files in the directory
find "$directory" -type f \( -name "*.db" -o -name "*.sqlite" \) | while read db_file; do

    # Extract the database name without the extension
    db_name=$(basename "$db_file" | sed 's/\.[^.]*$//')

    # Run the SQLite query to convert the database to CSV
    sqlite3 "$db_file" <<EOF
.headers on
.mode csv
.output "${db_name}.csv"
SELECT * FROM message;
EOF

done

