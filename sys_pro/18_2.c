#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <usistd.h>

int main(int argc, char* argv[]){
    char ch;
    close(0);
    close(1);
    open(argv[1],O_RDONLY);
    open(argv[2],O_WRONLY|O_CREAT|O_EXCL);

    while(scanf("%c", &ch) >0){
        printf("%c",ch);
    }
}