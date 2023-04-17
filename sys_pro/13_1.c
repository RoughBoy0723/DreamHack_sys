#include <stdio.h>
#include <stdlib.h>

int myStrlen(char *word){
    char buf;
    int cnt = 0;
    while(read(word,buf,1) > 0){
        cnt++;
        if(buf == NULL){
            break
        }
    }
    return cnt;
}

main(){
    printf("[%d]\n",myStrlen("This"));
    printf("[%d]\n",myStrlen("This is"));
    printf("[%d]\n",myStrlen("This is test"));
}