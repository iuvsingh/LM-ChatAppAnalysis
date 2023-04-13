#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h> // for chdir()

const char* COUNTER_FILE = "/sdcard/exe_files/counter.txt";
const char* DIR_PATH = "/sdcard/exe_files";
const char* DIFF_FILE = "/sdcard/exe_files/diff.txt";
const char* OLD_FILE = "/sdcard/exe_files/old_list.txt";
const char* NEW_FILE = "/sdcard/exe_files/new_list.txt";

int increment_counter() {
    char command[100];
    char count_str[10];
    int count = 0;
    FILE* pipe;

    // Check if the counter file exists in the specified directory and create it if necessary
    snprintf(command, sizeof(command), "[ -f %s ] || echo 0 > %s", COUNTER_FILE, COUNTER_FILE);
    system(command);

    // Read the current count from the file
    snprintf(command, sizeof(command), "cat %s", COUNTER_FILE);
    pipe = popen(command, "r");
    if (pipe != NULL) {
        fgets(count_str, sizeof(count_str), pipe);
        count = atoi(count_str);
        pclose(pipe);
    } else {
        printf("Error: Could not read counter file\n");
        return -1;
    }

    // Increment the counter and write the new value to the file
    count++;
    snprintf(command, sizeof(command), "echo %d > %s", count, COUNTER_FILE);
    system(command);

    return count - 1;
}

void check_or_create_dir(const char* dir_path) {
    char command[100];
    struct stat st;

    // Check if the directory exists
    if (stat(dir_path, &st) == -1) {
        // If the directory does not exist, create it
        mkdir(dir_path, 0777);
    }
}

// int main(int argc, char *argv[]) {
//     char command[100] = "cp -avr /data/data/";
//     char end_command[50] = " /sdcard/";
    
//     // Make directory
//     check_or_create_dir(DIR_PATH);

//     // // Create two files to keep track
//     char new_list_app[100] = "ls ~/data/data/ > ~/sdcard/exe_files/new_list.txt";
//     system(new_list_app);

//     int count = increment_counter();

//     if (count < 2) {
//         char old_list_app[50] = "touch /sdcard/exe_files/old_list.txt";
//         system(old_list_app);
//     }
    
//    // Compare old and new files
// 	char diff_command[100];
// 	snprintf(diff_command, sizeof(diff_command), "diff %s %s > %s", OLD_FILE, NEW_FILE, DIFF_FILE);
// 	int result = system(diff_command);

// 	// If the files are different, create a new file and overwrite the old file
// 	char *new_list_name="new_list";
// 	if (result != 0) {
// 	    char output_file[50];
// 	    snprintf(output_file, sizeof(output_file), "%s/%s.txt", DIR_PATH, new_list_name);

// 	    char copy_command[100];
// 	    snprintf(copy_command, sizeof(copy_command), "cp %s %s", NEW_FILE, output_file);
// 	    system(copy_command);

// 	    char mv_command[100];
// 	    snprintf(mv_command, sizeof(mv_command), "mv %s %s", NEW_FILE, OLD_FILE);
// 	    system(mv_command);
// 	}

//     // TEMP: concatenating which files to stage
//     strcat(command, argv[1]);
//     strcat(command, end_command);
//     system(command);
    
//     return 0;
// }



int main(int argc, char *argv[]) {

    char command[100] = "cp -avr /data/data/";
    char end_command[50] = " /sdcard/";
    
    // Make directory
    check_or_create_dir(DIR_PATH);

    // Create two files to keep track
    char new_list_app[50] = "ls /data/data/ > /sdcard/exe_files/new_list.txt";
    system(new_list_app);

    int count = increment_counter();
    printf("Count: %d\n", count);

    if (count < 2) {
        char old_list_app[50] = "touch /sdcard/exe_files/old_list.txt";
        system(old_list_app);
    }

    // Compare old and new files
	// Compare old and new files
	char cmp_command[100];
	snprintf(cmp_command, sizeof(cmp_command), "cmp -s %s %s > /dev/null", OLD_FILE, NEW_FILE);
	int result = system(cmp_command);

    printf("Result: %d\n", result);

    // If the files are different, create a new file and overwrite the old file
    char *new_list_name="new_list";
    if (result != 0) {
        printf("Files are different. Creating a new list file.\n");
        char output_file[50];
        snprintf(output_file, sizeof(output_file), "%s/%s.txt", DIR_PATH, new_list_name);
        printf("Output file: %s\n", output_file);

        char copy_command[100];
        snprintf(copy_command, sizeof(copy_command), "cp %s %s", NEW_FILE, output_file);
        printf("Copy command: %s\n", copy_command);
        system(copy_command);

        char mv_command[100];
        snprintf(mv_command, sizeof(mv_command), "mv %s %s", NEW_FILE, OLD_FILE);
        printf("Move command: %s\n", mv_command);
        system(mv_command);
    }

    // TEMP: concatenating which files to stage
    strcat(command, argv[1]);
    strcat(command, end_command);
    system(command);
    
    return 0;
}