#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char *argv[]){

    int pid;
    
    if(argc<3){
        printf("usage: a.out infile outfile");
        exit(0);
    }

    if(pid = fork() == 0){
        execl("/bin/cp",argv[1],argv[2], (char *) 0);
        exit(1);
    }else{
        wait((int *) 0);
        printf("child exited");
        exit(1);
    }

}