// Minimal cs50.c implementing get_int used by factorial program.
#include "cs50.h"
#include <limits.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int get_int(const char *format, ...) {
  va_list ap;
  char buf[1024];
  long val;
  char *endptr;

  while (1) {
    va_start(ap, format);
    vprintf(format, ap);
    va_end(ap);

    if (!fgets(buf, sizeof buf, stdin)) {
      return INT_MAX; // match cs50.h contract for EOF/error
    }

    // trim
    size_t len = strlen(buf);
    if (len > 0 && (buf[len - 1] == '\n' || buf[len - 1] == '\r'))
      buf[--len] = '\0';

    val = strtol(buf, &endptr, 10);
    if (endptr != buf && *endptr == '\0') {
      return (int)val;
    }

    // otherwise prompt again
  }
}
