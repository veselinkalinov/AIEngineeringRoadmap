#include <stdio.h>
#include <stdlib.h>

void iterdraw(int n);
void recursivedraw(int n);

int main(void) {
  int height = 0;

  printf("Height: ");
  if (scanf("%d", &height) != 1) {
    return 1;
  }

  iterdraw(height);
  printf("\n");
  recursivedraw(height);

  return 0;
}

// Iterative Func:

void iterdraw(int n) {
  // For each row
  for (int i = 0; i < n; i++) {
    // For each column
    for (int j = 0; j < i + 1; j++) {
      printf("#");
    }
    printf("\n");
  }
}

// Recursive Func:

void recursivedraw(int n) {

  // Base case
  if (n <= 0) {
    return;
  }

  // Print a pyramid of height n-1
  recursivedraw(n - 1);

  // Print one more row
  for (int i = 0; i < n; i++) {
    printf("#");
  }
  printf("\n");
}
