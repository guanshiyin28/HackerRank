#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
}

int main() { int n, k; int c = 0; int maxAnd = 0, maxOr = 0, maxXor = 0; scanf("%d %d", &n, &k);

for(int i=1; i<=n; i++){
    for(int j=i+1; j<=n; j++){
        c = i&j; 
        if(c > maxAnd && c < k) maxAnd = c;
    }
}
printf("%d\n", maxAnd);

for(int i=1; i<=n; i++){
    for(int j=i+1; j<=n; j++){
        c = i|j; 
        if(c > maxOr && c < k) maxOr = c;
    }
}
printf("%d\n", maxOr);

for(int i=1; i<=n; i++){
    for(int j=i+1; j<=n; j++){
        c = i^j; 
        if(c > maxXor && c < k) maxXor = c;
    }
}
printf("%d\n", maxXor);

return 0;

}
