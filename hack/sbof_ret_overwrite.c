#include <stdio.h>
#include <stdlib.h>

int main(void){
	char buf[8];

	printf("Overwrite return address with 0x4141414141414141: ");
	gets(buf);

	return 0;
}
