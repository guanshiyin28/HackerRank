#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char ch;
    char s[50];
    char sen[50];
    scanf("%c", &ch);
    scanf("%s", &s);
    scanf("\n");
    scanf("%[^\n]%*c",&sen);
    printf("%c\n%s\n%s",ch,s,sen);

return 0; }
