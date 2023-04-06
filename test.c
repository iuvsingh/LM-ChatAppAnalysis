#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h> // for chdir()

const char* OLD_FILE = "/sdcard/exe_files/old_list.txt";
const char* NEW_FILE = "/sdcard/exe_files/new_list.txt";
const char* DIFF_FILE = "/sdcard/exe_files/diff.txt";

//prototype
void check_or_create_dir();
void create_list_apps();
void staging_files();
void attachment_files();
void print_Asterisks();
void userInput();
void menu_option();
void cmp_files();

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
    fp_new=fopen("/sdcard/exe_files/new_list.txt", "r");
    system("touch /sdcard/exe_files/diff.txt")
    fp_diff=fopen("/sdcard/exe_files/diff.txt", "r");

    cmp_files()
}

void cmp_files(const char* file1, const char* file2, const char* output_file) {
    FILE *fp1, *fp2, *out;
    int ch1, ch2;

    fp1 = fopen(file1, "r");
    fp2 = fopen(file2, "r");
    out = fopen(output_file, "w");

    if (fp1 == NULL || fp2 == NULL || out == NULL) {
        printf("Error: Could not open file\n");
        return;
    }

    int line = 1, pos = 0, cmp_result = 0;

    do {
        ch1 = fgetc(fp1);
        ch2 = fgetc(fp2);

        if (ch1 == '\n' || ch2 == '\n') {
            if (ch1 != ch2) {
                cmp_result = 1;
                fprintf(out, "Line %d, Pos %d: ", line, pos);
                if (ch1 == EOF) {
                    fprintf(out, "%s: end of file, %s: %c\n", file1, file2, ch2);
                } else if (ch2 == EOF) {
                    fprintf(out, "%s: %c, %s: end of file\n", file1, ch1, file2);
                } else {
                    fprintf(out, "%s: %c, %s: %c\n", file1, ch1, file2, ch2);
                }
            }
            line++;
            pos = 0;
        } else if (ch1 != ch2) {
            cmp_result = 1;
            fprintf(out, "Line %d, Pos %d: %s: %c, %s: %c\n", line, pos, file1, ch1, file2, ch2);
        }
        pos++;
    } while (ch1 != EOF && ch2 != EOF);

    if (cmp_result == 0) {
        fprintf(out, "Files are identical\n");
    }

    fclose(fp1);
    fclose(fp2);
    fclose(out);
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