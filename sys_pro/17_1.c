#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char* argv[]){
    int fd1, cnt;
    fd1 = open(argv[1], O_RDWR);

    cnt = 0;
    lseek(fd1, argv[2], seek_set);
    write(fd1, argv[4], argv[3]);
}
//1. 반복문 돌리면서 즉각 바꿔주기   바꿔주는 함수 가 무엇인지
//2. 파일을 받아와서 부분만 바꿔주기  바꿔주기만하면됨