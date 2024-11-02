#include <stdio.h>
#include <stdlib.h>

int main() 
{
    int n;
    scanf("%d", &n);

    // Create a dynamic array of size n
    int* arr = (int*)malloc(n * sizeof(int));

    // Read the values from stdin and store them in the array
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Calculate the sum of all elements in the array
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    // Print the sum
    printf("%d\n", sum);

    // Free the memory where the array is stored
    free(arr);

    return 0;
}
