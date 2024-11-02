#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
  	char representation[9][10] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    for(int i=0; a+i <= b; i++) {
        printf("%s\n", a+i<=9 ? representation[a+i-1] : (a+i) % 2 ? "odd" : "even");
    }

    return 0;
}
