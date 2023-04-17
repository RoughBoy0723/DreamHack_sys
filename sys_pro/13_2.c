#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char* argv){
    int sum = 0;
    for(int i = 1 ; i < argc+1 ; i++){
        sum += atoi(argv[i])
    }
}