#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h> // for chdir()

const char* OLD_FILE = "/sdcard/exe_files/old_list.txt";
const char* NEW_FILE = "/sdcard/exe_files/new_list.txt";
const char* DIFF_FILE = "/sdcard/exe_files/diff.txt";
const char* FOLDER = "/sdcard/exe_files";

typedef enum { false, true } bool;

//prototype
void check_or_create_dir(const char* dir_path);
void create_list_apps();
int is_file_empty(const char *filename);
void compare_files(char *file1, char *file2, char *output_file);
void staging_files(char* arg1,char* arg2);
// void attachment_files();
// void print_Asterisks();
void userInput(char* arg1, char* arg2);
// void menu_option();
void kill_process();




void check_or_create_dir(const char* dir_path) {
    struct stat st;
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

    char *new_file = strdup(NEW_FILE);
    char *old_file = strdup(OLD_FILE);
    char *diff_file = strdup(DIFF_FILE);

    compare_files(new_file, old_file, diff_file);
    // compare_files(strdup(NEW_FILE),strdup(OLD_FILE),strdup(DIFF_FILE));

    // int check = is_file_empty(DIFF_FILE);
    // if (check==0){
    //     // print_Asterisks();
    //     printf("Following are the new packages discovered:\n\n");
    //     system("cat /sdcard/exe_files/diff.txt");
    // }

    free(new_file);
    free(old_file);
    free(diff_file);

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



void staging_files(char* arg1,char* arg2) {
    char input[100];
    char command[200] = "cp -avr ";
    char end_command[50] = " /sdcard/dbs_attchmnt";

    if (strcmp(arg1, "1") == 0) {
        // printf("Enter the application package name: ");
        // fgets(input, 100, stdin);
        // input[strcspn(input, "\n")] = '\0'; 

        check_or_create_dir("/sdcard/dbs_attchmnt");

        strcat(command, "/data/data/");
        strcat(command, arg2);
        strcat(command, end_command);
        // printf("%s\n",command);
        system(command);
    }
    else if (strcmp(arg1, "2") == 0) {
        // printf("Enter the path to attachment (include the \'/\'): ");
        // fgets(input, 100, stdin);
        // input[strcspn(input, "\n")] = '\0'; 

        check_or_create_dir("/sdcard/dbs_attchmnt");

        strcat(command, arg2);
        strcat(command, end_command);
        // printf("%s\n",command);
        system(command);
    }
    else {
        printf("Invalid operation!\n");
    }
}



// void staging_files(char* arg1){
//     char input[100];
//     char command[100] = "cp -avr /data/data/";
//     char end_command[50] = " /sdcard/";

//     // printf("Enter the application package name: ");
//     // fgets(input, 100, stdin);
//     // input[strcspn(input, "\n")] = '\0'; 

//     strcat(command, arg1);
//     strcat(command, end_command);
//     // printf("%s\n\n",command);
//     system(command);
// }

// void attachment_files(char* arg1){
//     char input[100];
//     char command[100] = "cp -avr ";
//     char end_command[50] = " /sdcard/";

//     // printf("Enter the path to attachment (include the \'/\'): ");
//     // fgets(input, 100, stdin);
//     // input[strcspn(input, "\n")] = '\0'; 

//     strcat(command, arg1);
//     strcat(command, end_command);
//     // printf("%s\n\n",command);
//     system(command);
// }

// //Print asteriks to create menu
// void print_Asterisks() {
//     int i;

//     for (i = 0; i < 50; i++) {
//         printf("*");
//     }

//     printf("\n");
// }

// //Create menu
// void menu_option(){
//     print_Asterisks();
//     printf("WELCOME\n\n");
//     printf("Select an option below\n\n");
//     printf("1 - Export the database files\n");
//     printf("2 - Export the attachment\n");
//     printf("3 - View new apps\n");
//     printf("4 - Quit\n\n");
//     print_Asterisks();
//     printf("Please enter your option: ");
// }


//Ask for user input
void userInput(char* arg1, char* arg2) {
    // char input[100];
    int quit = 0;


    // menu_option();
    // fgets(input, sizeof(input), stdin);
    // input[strcspn(input, "\n")] = '\0';  // remove newline character

    check_or_create_dir(FOLDER);
    create_list_apps();

    //Quitting options
    if (strcmp(arg1, "3") == 0 || strcmp(arg1, "q") == 0 || strcmp(arg1, "Q") == 0 || strcmp(arg1, "quit") == 0 || strcmp(arg1, "exit") == 0) {
        quit = 1;
    }else if (strcmp(arg1,"1")==0 || strcmp(arg1,"2")==0) {
        staging_files(arg1,arg2);
    
    // }else if (strcmp(arg1,"3")==0) {
    //     check_or_create_dir(FOLDER);
    //     create_list_apps();
    // // }else if (strcmp(arg1, "cls") == 0 || strcmp(arg1, "clear") == 0){
    // //     system("clear");
    // }
    }else {
        // print_Asterisks();
        printf("! Invalid Option !\n");
    }
    
    kill_process();
    // printf("Exiting...\n");
}

void kill_process(){
    char kill_copydbf[150]="killall -9 //data/local/tmp/./copydbF 2>/dev/null";
    // char kill_perm[100]="killall -9 /data/local/tmp/./permissions";

    // system(kill_perm);
    system(kill_copydbf);

}

int main(int argc, char *argv[]) {

    //arg1 = option number, arg2 = data path
    userInput(argv[1], argv[2]);

    return 0;
}