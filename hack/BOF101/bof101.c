#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int printflag(){ 
	char buf[32];
	FILE* fp = fopen("/flag", "r"); 
	fread(buf, 1, 32, fp);
	fclose(fp);
	printf("%s", buf);
	return 0;
}

int main() {
	int check=0xdeadbeef; 8byte
	char name[140];
	printf("printflag()'s addr: %p\n", &printflag);
	printf("What is your name?\n: ");
	scanf("%s", name);	
	if (check != 0xdeadbeef){
		printf("[Warning!] BOF detected!\n");
		exit(0);
	}
	return 0;
}


128 64 32 16
144ch
