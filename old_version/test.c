#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h> // for chdir()

const char* OLD_FILE = "/sdcard/exe_files/old_list.txt";
const char* NEW_FILE = "/sdcard/exe_files/new_list.txt";
const char* DIFF_FILE = "/sdcard/exe_files/diff.txt";

typedef enum { false, true } bool;

//prototype
void check_or_create_dir();
void create_list_apps();
void staging_files();
void attachment_files();
void print_Asterisks();
void userInput();
void menu_option();
void compare_files();
int is_file_empty(const char *filename);

void check_or_create_dir() {
    struct stat st;
    char dir_path[100]="/sdcard/exe_files";
    // Check if the directory exists
    if (stat(dir_path, &st) == -1) {
        // If the directory does not exist, create it
        mkdir(dir_path, 0777);
    }
}

void create_list_apps(){
    FILE *fp_old, *fp_new, *fp_diff;
    fp_old = fopen("/sdcard/exe_files/old_list.txt", "r");
    if (fp_old == NULL)
    {
        system("ls /data/data > /sdcard/exe_files/old_list.txt");
        printf("New file created successfully!\n");
        // fclose(fp);
        // return;
    }
    // printf("File already exists!\n");
    system("ls /data/data > /sdcard/exe_files/new_list.txt");
    system("touch /sdcard/exe_files/diff.txt");

    compare_files(NEW_FILE,OLD_FILE,DIFF_FILE);

    int check = is_file_empty(DIFF_FILE);
    if (check==0){
        print_Asterisks();
        printf("Following are the new packages discovered:\n\n");
        system("cat /sdcard/exe_files/diff.txt");
    }

}

int is_file_empty(const char *file_path) {
    struct stat st;
    if (stat(file_path, &st) != 0) {
        return -1; // error occurred
    }
    return st.st_size == 0;
}

void compare_files(char *file1, char *file2, char *output_file) {
    FILE *fp1, *fp2, *fout;
    char line1[1024], line2[1024];
    int line_num = 0;
    bool change_detected = false;

    // open the input files
    fp1 = fopen(file1, "r");
    if (fp1 == NULL) {
        printf("Error opening file %s\n", file1);
    }

    fp2 = fopen(file2, "r");
    if (fp2 == NULL) {
        printf("Error opening file %s\n", file2);
    }

    // open the output file
    fout = fopen(output_file, "w");
    if (fout == NULL) {
        printf("Error creating file %s\n", output_file);
    }

    // read from file1 and compare with file2
    while (fgets(line1, sizeof(line1), fp1) != NULL) {
        change_detected = false;

        // search for line1 in file2
        while (fgets(line2, sizeof(line2), fp2) != NULL) {
            if (strcmp(line1, line2) == 0) {
                change_detected = true;
                break;
            }
        }

        // reset file2
        fseek(fp2, 0, SEEK_SET);

        // write line1 to output file if it doesn't match any line in file2
        if (!change_detected) {
            fprintf(fout, "%s", line1);
        }
    }
    // close the files
    fclose(fp1);
    fclose(fp2);
    fclose(fout);
}


void staging_files(){
    char input[100];
    char command[100] = "cp -avr /data/data/";
    char end_command[50] = " /sdcard/";

    printf("Enter the application package name: ");
    fgets(input, 100, stdin);
    input[strcspn(input, "\n")] = '\0'; 

    strcat(command, input);
    strcat(command, end_command);
    printf("%s\n\n",command);
    // system(command);
}

void attachment_files(){
    char input[100];
    char command[100] = "cp -avr ";
    char end_command[50] = " /sdcard/";

    printf("Enter the path to attachment (include the \'/\'): ");
    fgets(input, 100, stdin);
    input[strcspn(input, "\n")] = '\0'; 

    strcat(command, input);
    strcat(command, end_command);
    printf("%s\n\n",command);
    // system(command);
}

//Print asteriks to create menu
void print_Asterisks() {
    int i;

    for (i = 0; i < 50; i++) {
        printf("*");
    }

    printf("\n");
}

//Create menu
void menu_option(){
    print_Asterisks();
    printf("WELCOME\n\n");
    printf("Select an option below\n\n");
    printf("1 - Export the database files\n");
    printf("2 - Export the attachment\n");
    printf("3 - View new apps\n");
    printf("4 - Quit\n\n");
    print_Asterisks();
    printf("Please enter your option: ");
}

//Ask for user input
void userInput() {
    char input[100];
    int quit = 0;

    while (!quit) {
        menu_option();
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';  // remove newline character

        //Quitting options
        if (strcmp(input, "4") == 0 || strcmp(input, "q") == 0 || strcmp(input, "Q") == 0 || strcmp(input, "quit") == 0 || strcmp(input, "exit") == 0) {
            quit = 1;
        } else if (strcmp(input,"1")==0) {
            staging_files();
        }else if (strcmp(input,"2")==0) {
            attachment_files();
        }else if (strcmp(input,"3")==0) {
            check_or_create_dir();
            create_list_apps();
        }else if (strcmp(input, "cls") == 0 || strcmp(input, "clear") == 0){
            system("clear");
        }
        else {
            print_Asterisks();
            printf("! Invalid Option !\n");
        }
    }

    printf("Exiting...\n");
}


int main(int argc, char *argv[]) {
    userInput();
}