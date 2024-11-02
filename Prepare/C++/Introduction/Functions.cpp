#include <stdio.h>

int max(int arr[4]) {
    int maximum = arr[0];
    for (int i = 1; i < 4; i++) {
        if (arr[i] > maximum) {
            maximum = arr[i];
        }
    }
    return maximum;
}

int main() {
    int arr[4];
    
    for (int i = 0; i < 4; i++) {
        scanf("%d", &arr[i]);
    }
    
    printf("%d\n", max(arr));
    
    return 0;
}
