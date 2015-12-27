#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
void push(uint16_t);
void add();
void sub();
void out();
void dup();
uint16_t peek();
#define NOP 0
#define ADD 1
#define SUB 2
#define OUT 3
#define IN 4
#define DUP 5
#define PUSH 128

