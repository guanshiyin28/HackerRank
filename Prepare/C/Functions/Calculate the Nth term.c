#include<stdio.h>

int main() {
    int n, a, b, c;

    scanf("%d", &n);
    scanf("%d %d %d", &a, &b, &c);

    int last_three[3];
    last_three[0] = a;
    last_three[1] = b;
    last_three[2] = c;

    int sum = last_three[0] + last_three[1] + last_three[2];

    if (n==3) {
        printf("%d", c);
    }

    else if (n==2){
        printf("%d", b);
    }

    else if (n==1){
        printf("%d", a);
    }

    else {
        
    for (int i = 3; i < n-1; i++) {
        last_three[0] = last_three[1];
        last_three[1] = last_three[2];
        last_three[2] = sum;

        sum = last_three[0] + last_three[1] + last_three[2];
    }

    printf("%d\n", sum);
    }

    return 0;
}
