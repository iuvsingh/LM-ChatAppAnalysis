#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h> 

//creating variables for files
const char* OLD_FILE = "/sdcard/exe_files/old_list.txt";
const char* NEW_FILE = "/sdcard/exe_files/new_list.txt";
const char* DIFF_FILE = "/sdcard/exe_files/diff.txt";
const char* FOLDER = "/sdcard/exe_files";

typedef enum { false, true } bool;

//prototype
void check_or_create_dir(const char* dir_path);
void create_list_apps(char* clear_opt);
int is_file_empty(const char *filename);
void compare_files(char *file1, char *file2, char *output_file,char* clear_opt);
void staging_files(char* arg1,char* arg2);
void userInput(char* arg1, char* arg2);
void kill_process();
void replace_file(char *file1, char *file2);



void check_or_create_dir(const char* dir_path) {
    struct stat st;
    // Check if the directory exists
    if (stat(dir_path, &st) == -1) {
        // If the directory does not exist, create it
        mkdir(dir_path, 0777);
    }
}

//creates list of new apps
void create_list_apps(char* clear_opt){
    FILE *fp_old, *fp_new, *fp_diff;
    fp_old = fopen("/sdcard/exe_files/old_list.txt", "r");
    //if the old_lists.txt file does not exist
    if (fp_old == NULL)
    {
        //creates old_lists.txt by redirecting ls output to file
        system("ls /data/data > /sdcard/exe_files/old_list.txt");
        printf("New file created successfully!\n");
      
    }
    //if old_lists.txt does exist, new_list.txt file is created 
    system("ls /data/data > /sdcard/exe_files/new_list.txt");
    //creates a diff.txt file
    system("touch /sdcard/exe_files/diff.txt");

    char *new_file = strdup(NEW_FILE);
    char *old_file = strdup(OLD_FILE);
    char *diff_file = strdup(DIFF_FILE);

    //compares the new and old text file and outputs to difference into the diff_file
    compare_files(new_file, old_file, diff_file,clear_opt);
    
    //free the space in these files
    free(new_file);
    free(old_file);
    free(diff_file);

}

//checks if file at given path is empty or not and returns the 0 if not empty
int is_file_empty(const char *file_path) {
    struct stat st;
    if (stat(file_path, &st) != 0) {
        return -1; // error occurred
    }
    return st.st_size == 0;
}

//function to compare the files 
void compare_files(char *file1, char *file2, char *output_file,char* clear_opt) {
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
    if (strcmp(clear_opt, "y") == 0) {
        fout = fopen(output_file, "w");
        if (fout == NULL) {
            printf("Error creating file %s\n", output_file);
        }
    } else {
        fout = fopen(output_file, "a");
        if (fout == NULL) {
            printf("Error opening file %s\n", output_file);
        }
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

    replace_file(file1,file2);

    // close the files
    fclose(fp1);
    fclose(fp2);
    fclose(fout);
}

void replace_file(char *file1, char *file2) {
    FILE *fp1, *fp2;
    char line[1024];

    // open the input files
    fp1 = fopen(file1, "r");
    if (fp1 == NULL) {
        printf("Error opening file %s\n", file1);
    }

    fp2 = fopen(file2, "w");
    if (fp2 == NULL) {
        printf("Error creating file %s\n", file2);
    }

    // read from file1 and write to file2
    while (fgets(line, sizeof(line), fp1) != NULL) {
        fprintf(fp2, "%s", line);
    }

    // close the files
    fclose(fp1);
    fclose(fp2);
}


//function for staging files
void staging_files(char* arg1,char* arg2) {
    char input[100];
    char command[200] = "cp -avr ";
    char end_command[50] = " /sdcard/dbs_attchmnt";
    //if the user input option is 1
    if (strcmp(arg1, "1") == 0) {
        

        check_or_create_dir("/sdcard/dbs_attchmnt");
        //copies the file path of the package specified by the user input into the end_command directory
        strcat(command, "/data/data/");
        strcat(command, arg2);
        strcat(command, end_command);
        // printf("%s\n",command);
        system(command);
    }
    //if the user input option is 2
    else if (strcmp(arg1, "2") == 0) {
       

        check_or_create_dir("/sdcard/dbs_attchmnt"); 
        //copies the file path of the attachment into the end_command directory 
        strcat(command, arg2);
        strcat(command, end_command);
        system(command);
    }
    else {
        printf("Invalid operation!\n");
    }
}





//Ask for user input
void userInput(char* arg1, char* arg2) {
    // char input[100];
    int quit = 0;



    check_or_create_dir(FOLDER);
    create_list_apps(arg2);

    //Quitting options
    if (strcmp(arg1, "3") == 0 || strcmp(arg1, "q") == 0 || strcmp(arg1, "Q") == 0 || strcmp(arg1, "quit") == 0 || strcmp(arg1, "exit") == 0) {
        quit = 1;
    //Staging options
    }else if (strcmp(arg1,"1")==0 || strcmp(arg1,"2")==0) {
        staging_files(arg1,arg2);
    //Create diff.txt list
    }else if (strcmp(arg1,"3")==0) {
        check_or_create_dir(FOLDER);
        create_list_apps(arg2);
   
    }else {
        // print_Asterisks();
        printf("! Invalid Option !\n");
    }
    
    kill_process();
}

//end ndk executable process
void kill_process(){
    char kill_copydbf[150]="killall -9 //data/local/tmp/./copydbF 2>/dev/null";
 
    system(kill_copydbf);

}

int main(int argc, char *argv[]) {

    //arg1 = option number, arg2 = data path
    userInput(argv[1], argv[2]);

    return 0;
}