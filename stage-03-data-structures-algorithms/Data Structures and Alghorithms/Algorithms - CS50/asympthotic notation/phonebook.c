#include <stdio.h>
#include <string.h>

typedef struct {
  char *name;
  char *number;
} Person;

int main(void) {
  Person people[3];
  people[0].name = "Kelly";
  people[0].number = "+1-617-495-1000";

  people[1].name = "David";
  people[1].number = "+1-617-495-1000";

  people[2].name = "John";
  people[2].number = "+1-949-468-2750";

  char name[128];
  printf("Name: ");
  if (!fgets(name, sizeof name, stdin))
    return 1;
  // remove trailing newline
  name[strcspn(name, "\n")] = '\0';

  for (int i = 0; i < 3; i++) {
    if (strcmp(people[i].name, name) == 0) {
      printf("Found %s\n", people[i].number);
      return 0;
    }
  }
  printf("Not found\n");
  return 1;
}
