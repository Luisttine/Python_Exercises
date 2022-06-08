#include <stdio.h>
#include <unistd.h>
#include <stdbool.h>

int main(void){
	
	while(true){
		printf("\nProcessando . . .\n");
		sleep(2);
		
		printf("%c", getchar());
	}
	
	return 0;
}
