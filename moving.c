#include <stdio.h>
#include <stdlib.h>	//to use system()
#include <string.h>	
#include <dirent.h>

#define MAX_LINE_LENGTH 1000

void change_in_file() {

    // Pointer structer of type dirent (directory entry)
    struct dirent *directory_entry; 

	// opening current directory 
    DIR *directory = opendir(".");
    
	// if current directory fails to open. Print error and exist
    if (directory == NULL) {
        printf("Error: Could not open current directory.\n");
        return 1;
    }

	// enter file name you want to go with
	char *filename1 = "InitialList.txt";
	char *filename2 = "SecondList.txt";
	
	// Declaring FILE variables for opening and closing the file.
	FILE *file1, *file2, *checkf1, *checkf2;
        
	// this loop will check each file/directory with our two files. if file provided with our name is matched it will create file reading object
	while ((directory_entry = readdir(directory)) != NULL) {
		// if file1 exist with same name open the file in read & write mood.
        if (strcmp(directory_entry->d_name, filename1) == 0) {
            file1 = fopen(filename1, "r");
            // if file1 failed to open return with error message
            if (file1 == NULL) {
                printf("Error: Could not open %s.\n", filename1);
                return 1;
            }
        }
        // if file2 exist with same name open the file in read mood.
        if (strcmp(directory_entry->d_name, filename2) == 0) {
            file2 = fopen(filename2, "r+");
            // if file2 failed to open return with error message
            if (file2 == NULL) {
                printf("Error: Could not open %s.\n", filename2);
                return 1;
            }
        }
    }
    
    // checking if file1 exists or not in current directory. Return error if no file1 exists.
	checkf1 = fopen(filename1, "r");
    if (checkf1 == NULL) {
        printf("Error: %s not found in current directory.\n", filename1);
        return 1;
    }
    
    // checking if file1 exists or not in current directory. Return error if no file2 exists.
    checkf2 = fopen(filename2, "r");
    if (checkf2 == NULL) {
        printf("Error: %s not found in current directory.\n", filename2);
        return 1;
    }

    
	// declaring two line arrays with max line length of 1000
	char line1[MAX_LINE_LENGTH], line2[MAX_LINE_LENGTH];
    
    // declaring two int varaibles for match_found and for new_content found
	int match_found, new_content_found = 0;
    
    // loop through each line of file1 and check either it at the end of line or not.
	while (fgets(line1, MAX_LINE_LENGTH, file1) != NULL) {
        // flag to check match_found or not
		match_found = 0;
        
        // reset the file indication position for file2
        rewind(file2);
        
    	// loop through each line of file2 and check either it at the end of line or not.
        while (fgets(line2, MAX_LINE_LENGTH, file2) != NULL) {
            // compare file2 line by line with line of file 1. If match found then flag will go up and break the loop
			if (strcmp(line1, line2) == 0) {
                match_found = 1;
                break;
            }
        }
        // if no match found that means new content is there in file1 that will be added to file2.
        if (!match_found) {
            new_content_found = 1;
            // adding new from file1 
            fputs(line1, file2);
        }
    }

	// print new content found in file.txt or not and added to file2.txt
    if (!new_content_found) {
        printf("No new content found in %s.\n", filename1);
    } else {
        printf("New content added to %s.\n", filename2);
    }

	// closing all opened files
    fclose(checkf1);
    fclose(checkf2);
	fclose(file1);
    fclose(file2);
    return 0;
}


int main(int argc, char *argv[])
{
	char command[100]="cp -avr /data/data/";
	char end_command[50]=" /sdcard/";
	
	strcat(command,argv[1]);
    strcat(command,end_command);
	
	//system(command);
	system("ls /data/data/ > InitialList.txt");
	system("touch SecondList.txt")
	change_in_file();

	return 0;
}

