#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int CAPACITY = 50;

typedef struct {
  char people[CAPACITY];
  int size;
} stack;
