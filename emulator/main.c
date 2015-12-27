#include <stdio.h>
#include "cpu.h"
FILE *fileptr;
char *buffer;
long filelen;
char* currentByte;	
int decodeInstruction(){
	char op = *currentByte++;
	if(op&128){
		uint16_t val= ((op&127)<<8) + *currentByte++;
		push(val);
		return 2;
	}
	switch(op){
		case NOP: break;
		case ADD:add(); break;
		case SUB:sub(); break;
		case OUT:out(); break;
		case DUP:dup(); break;
	}
	return 1;

}
int main(int argc, char** argv){
	if(argc != 2){
		puts("Usage sim [program]");
		return -1;
	}
		
	

	fileptr = fopen(argv[1], "rb");  // Open the file in binary mode
	fseek(fileptr, 0, SEEK_END);          // Jump to the end of the file
	filelen = ftell(fileptr);             // Get the current byte offset in the file
	rewind(fileptr);                      // Jump back to the beginning of the file

	buffer = (char *)malloc((filelen+1)*sizeof(char)); // Enough memory for file + \0
	fread(buffer, filelen, 1, fileptr); // Read in the entire file
	fclose(fileptr); // Close the file
	int i=0;
	
	currentByte = buffer;
	while(i<filelen){
		i+= decodeInstruction();
		//printf("TOS: %d\n",peek());
	
	}
	
	
	
	return 0;
}
