#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h> // for chdir()

// int main(int argc, char *argv[]){
//     char assign_perm[100] = "chmod +x /data/local/tmp/copydbF";
//     char move[100] = "cp -rvf /sdcard/copydbF /data/local/tmp/";
//     char exe_run[100]="/data/local/tmp/./copydbF";
    
//     system(move);
//     system(assign_perm);
//     system(exe_run);

//     return 0;
// }

int main(int argc, char *argv[]){
    char assign_perm[100] = "chmod +x /data/local/tmp/copydbF";
    char move[100] = "cp -rvf /sdcard/copydbF ~/data/local/tmp/";
    char exe_run[100]="~/data/local/tmp/./copydbF";
    // char exe_run[100]="x-terminal-emulator -e 'bash -c \"~/data/local/tmp/./copydbF\"'";
    //-e \'bash -c \"~/Desktop/./moving\"\' &
    
    system(move);
    system(assign_perm);

    FILE *output = popen(exe_run, "r");
    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), output)) {
        printf("%s", buffer);
    }
    pclose(output);

    return 0;
}