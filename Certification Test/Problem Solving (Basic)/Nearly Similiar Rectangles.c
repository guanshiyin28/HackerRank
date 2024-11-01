#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);
char** split_string(char*);

int parse_int(char*);
long parse_long(char*);



/*
 * Complete the 'nearlySimilarRectangles' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts 2D_LONG_INTEGER_ARRAY sides as parameter.
 */
 
 
// Comparison function for qsort
int cmpfunc(const void *a, const void *b) {
    return (*(double*)a - *(double*)b);
}

long nearlySimilarRectangles(int sides_rows, int sides_columns, long** sides) {
    // Assuming epsilon = 0.01 (adjust as needed)
    double epsilon = 0.01;

    // Calculate ratios and store them in a sorted array
    double *ratios = (double*)malloc(sides_rows * sizeof(double));
    for (int i = 0; i < sides_rows; i++) {
        long a = sides[i][0], b = sides[i][1];
        ratios[i] = (double)fmax(a, b) / fmin(a, b);
    }
    qsort(ratios, sides_rows, sizeof(double), cmpfunc);

    // Count nearly similar pairs
    long count = 0;
    for (int i = 0; i < sides_rows; i++) {
        double lower = ratios[i] * (1 - epsilon);
        double upper = ratios[i] * (1 + epsilon);
        int j = i + 1;
        while (j < sides_rows && ratios[j] <= upper) {
            count++;
            j++;
        }
    }
    return count / 2; // Divide by 2 to avoid double-counting
}



int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    int sides_rows = parse_int(ltrim(rtrim(readline())));

    int sides_columns = parse_int(ltrim(rtrim(readline())));

    long** sides = malloc(sides_rows * sizeof(long*));

    for (int i = 0; i < sides_rows; i++) {
        *(sides + i) = malloc(sides_columns * (sizeof(long)));

        char** sides_item_temp = split_string(rtrim(readline()));

        for (int j = 0; j < sides_columns; j++) {
            long sides_item = parse_long(*(sides_item_temp + j));

            *(*(sides + i) + j) = sides_item;
        }
    }

    long result = nearlySimilarRectangles(sides_rows, sides_columns, sides);

    fprintf(fptr, "%ld\n", result);

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;

    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data) {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);

        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }

    return data;
}

char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    while (*str != '\0' && isspace(*str)) {
        str++;
    }

    return str;
}

char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    char* end = str + strlen(str) - 1;

    while (end >= str && isspace(*end)) {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);

        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}

long parse_long(char* str) {
    char* endptr;
    long value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}
