/* Minimal copy of cs50.h for local libcs50 build */
#ifndef CS50_H
#define CS50_H

#include <limits.h>
#include <stdarg.h>


typedef char *string;

int get_int(const char *format, ...) __attribute__((format(printf, 1, 2)));

#endif // CS50_H
