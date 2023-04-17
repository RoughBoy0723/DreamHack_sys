#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char *argv[]){
    int fd1, fd2;
    char buf;

    fd1 = open(argv[1], O_RDONLY);
    fd2 = open(argv[2],O_WRONLY|O_CREAT|O_TRUNC);

    while(read(fd1,buf,1)>0){
        buf = buf + 3;
        write(fd2,buf,1);
    }
}