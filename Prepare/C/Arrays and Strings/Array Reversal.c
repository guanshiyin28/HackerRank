#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i,j,box;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);  
    }
    if(num%2==0){
    for(j=0;j<num/2;j++){
       box=arr[j];
       arr[j]=arr[num-1 -j];
       arr[num-1-j]=box;
    }
    }
    else{
        for(j=0;j<(num-1)/2;j++){
         box=arr[j];
         arr[j]=arr[num-1 -j];
        arr[num-1-j]=box;
    }
    }
   
    
    /* Write the logic to reverse the array. */

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}
