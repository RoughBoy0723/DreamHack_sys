#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char *argv[]){
    int fd1;
    char buf[256];

    fd1 = open(argv[1], O_WRONLY,0666);
    
    while(1){
        scanf("%s",&buf);
        if(buf == '.')
            break;
        write(fd1, buf, 1);
    }
}