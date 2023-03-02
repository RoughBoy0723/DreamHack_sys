#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

const char* binsh = "/bin/sh";

int main(){
	char buf[0x30];
	
	setvbuf(stdin, 0, _IONBF, 0);
	setvbuf(stdout, 0, _IONBF, 0);

	system("echo 'ststem@plt'");

	printf("[1] Leak Canary\n");
	printf("Buf: ");
	read(0, buf, 0x100);
	printf("Buf: %s\n", buf);

	printf("[2] Overwrite return addres\n");
	printf("Buf: ");
	read(0, buf, 0x100);

	return 0;
}
