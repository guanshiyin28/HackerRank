#include <iostream>
#include <deque> 
using namespace std;

int getHighest(const int arr[],const int &startIndex, const int &endIndex, int &outIndex) {
    int high=-1;
    for (int cnt=startIndex ; cnt<=endIndex ; cnt++) {
        if (arr[cnt]>=high) { // Yes do equal as well since we wnt the furtest index
            high = arr[cnt] ;
            outIndex = cnt ;
        }
    }
    return high;
}

void printKMax(int arr[], int n, int k){
    //Write your code here.
    int startIndex=0;
    int endIndex=k-1;
    int highIndex;
    int higestNumber;
    higestNumber=getHighest(arr,startIndex,endIndex,highIndex);
    std::cout << higestNumber << ' ';
    while (endIndex<n-1) {
        if (highIndex==startIndex) { // Oeps we need to recalculate
            startIndex++ ; endIndex++ ;
            higestNumber=getHighest(arr,startIndex,endIndex,highIndex);
            std::cout << higestNumber << ' ';
            continue;
        }
        startIndex++; endIndex++;
        if (arr[endIndex]>=higestNumber) {
            higestNumber = arr[endIndex] ;
            highIndex = endIndex;
        }
        std::cout << higestNumber << ' ';
    }
    std::cout << std::endl;
}


int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}
