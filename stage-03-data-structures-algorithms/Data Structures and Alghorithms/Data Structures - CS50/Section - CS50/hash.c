#include <ctype.h>
#include <stdio.h>
#include <string.h>

#define MAX_WORD_LENGTH 100

int hash(char *word);

int main(void) {
  char word[MAX_WORD_LENGTH + 1];

  printf("Word: ");
  if (fgets(word, sizeof(word), stdin) == NULL) {
    return 1;
  }

  word[strcspn(word, "\n")] = '\0';
  printf("Hash value: %i\n", hash(word));
}

// Hash the word based on the first two letters of the word
int hash(char *word) {
  // Word is less than 2 letters
  if (word == NULL || strlen(word) < 2) {
    return -2;
  }

  unsigned char c = (unsigned char)word[0];
  unsigned char c1 = (unsigned char)word[1];

  if (isalpha(c) && isalpha(c1)) {
    c = toupper(c);
    c1 = toupper(c1);
    return (c - 'A') * 100 + c1 - 'A';
  }

  return -1;
}
