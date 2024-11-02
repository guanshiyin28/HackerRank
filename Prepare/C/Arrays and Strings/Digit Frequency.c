#include <stdio.h>
#include <string.h>

int main() {
    char str[1000];
    int count=0;
    char num_arr[10]={'0','1','2','3','4','5','6','7','8','9'};
    scanf("%s",str);
    for(int i=0;i<10;i++){ 
        count=0;    //assigning count=0 for each digit 0-9
        for(int j=0;j<strlen(str);j++){
            if(str[j]==num_arr[i]){ //find occurences of each digit in given string 
                count++;
            }
        }
        printf("%d ",count);
    }
    
    return 0;
}
