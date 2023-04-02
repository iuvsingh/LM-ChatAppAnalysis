#include <stdio.h>
#include <stdlib.h>	//to use system()
#include <string.h>	
//#include <dirent.h>

// #define BUILD_COUNTER_FILE "build_counter.txt"
// #define MAX_COUNT 2

// int increment_build_counter() {
//     FILE* file;
//     int count = 0;

//     // Open the file for reading
//     file = fopen(BUILD_COUNTER_FILE, "r");
//     if (file != NULL) {
//         // Read the current count from the file
//         fscanf(file, "%d", &count);
//         fclose(file);
//     }

//     // Open the file for writing and increment the count
//     file = fopen(BUILD_COUNTER_FILE, "w");
//     if (file != NULL) {
//         fprintf(file, "%d", count + 1);
//         fclose(file);
//     }
    
//     return count;
// }

// char* diff_files() {
//     char command[100];
//     char buffer[256];
//     char* result = NULL;
//     FILE* pipe;

//     // Build the command string with hardcoded file names
//     sprintf(command, "diff file1.txt file2.txt");

//     // Open the command as a pipe and read the output
//     pipe = popen(command, "r");
//     if (!pipe) {
//         printf("Error executing command\n");
//         return NULL;
//     }

//     while (fgets(buffer, sizeof(buffer), pipe) != NULL) {
//         // Allocate memory for the result string
//         if (result == NULL) {
//             result = (char*)malloc(strlen(buffer) + 1);
//             strcpy(result, buffer);
//         }
//         else {
//             // Expand the result string
//             result = (char*)realloc(result, strlen(result) + strlen(buffer) + 1);
//             strcat(result, buffer);
//         }
//     }

//     // Close the pipe and print the status
//     int status = pclose(pipe);
//     if (status == -1) {
//         printf("Error closing pipe\n");
//     }
//     else {
//         printf("Command exited with status %d\n", status);
//     }

//     return result;
// }

int main(int argc, char *argv[])
{
	char command[100]="cp -avr /data/data/";
	char end_command[50]=" /sdcard/";
	
	// //Create two files to keep track
	// char new_list_app[50]="touch new_list.txt";
	
	// int count = increment_build_counter();
	
	// if (count < 2) {
	// 	char old_list_app[50]="touch old_list.txt";
	// 	system(old_list_app);
	// 	}
	
	//TEMP: concatenating which files to stage
	strcat(command,argv[1]);
    strcat(command,end_command);
	system(command);
	
	//execute the new file
	// system(new_list_app);
	
	return 0;
}

