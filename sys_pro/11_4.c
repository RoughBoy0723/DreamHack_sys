#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char *argv[]){
    int pid;
    if(pid = fork() == 0){
        print("Hello, World\n");
        exit(10);
    }else{
        wait((int *) 0);
        print("%d", pid);
        exit(0x00)
    }

}