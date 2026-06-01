#include <cs50.h>
#include <stdio.h>


int fib(int n);

int main(void) {
  int n = get_int("Fibonacci number: ");
  printf("The %ith Fibonacci number is %i\n", n, fib(n));
}

// Takes which fibonacci number you want, and then returns that
int fib(int n) {
  // Base case
  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 1;
  }

  // Recursive case
  return fib(n - 1) + fib(n - 2);
}
