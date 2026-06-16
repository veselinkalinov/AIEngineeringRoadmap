#include <ctype.h>

int hash(const char *name) { return toupper(name[0]) - 'A'; }
