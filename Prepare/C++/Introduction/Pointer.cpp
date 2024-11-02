#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function 
    int aa = *a;
    int bb = *b;   
    *a = aa + bb;
    *b = aa > bb ? (aa - bb) : (bb - aa);
}


int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
