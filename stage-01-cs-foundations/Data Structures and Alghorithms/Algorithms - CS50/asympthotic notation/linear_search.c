#include <stdio.h>
#include <string.h>

// Replaced cs50 get_string dependency with standard C input

// Big O(n)

// int main(void) {
//   int numbers[] = {20, 500, 10, 5, 100, 1, 50};

//   int n = get_int("Number: ");
//   for (int i = 0; i < 7; i++) {
//     if (numbers[i] == n) {
//       printf("Found\n");
//       return 0;
//     }
//   }
//   printf("Not found\n");
//   return 1;
// }

int main(void) {
  char *strings[] = {"battleship", "boot",    "cannon",
                     "iron",       "thimble", "top hat"};

  char s[100];
  printf("String: ");
  if (scanf("%99s", s) != 1) {
    printf("Not found\n");
    return 1;
  }

  for (int i = 0; i < 6; i++) {
    if (strcmp(strings[i], s) == 0) {
      printf("Found\n");
      return 0;
    }
  }
  printf("Not found\n");
  return 1;
}
