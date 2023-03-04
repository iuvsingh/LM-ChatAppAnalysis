#include <stdio.h>
#include <stdlib.h>	//to use system()
#include <string.h>	

int main(int argc, char *argv[])
{
	char command[100]="cp -avr /data/data/";
	char end_command[50]=" /sdcard/";
	
	strcat(command,argv[1]);
    	strcat(command,end_command);
	
	//printf("%s",command);
	
	system(command);

	return 0;
}