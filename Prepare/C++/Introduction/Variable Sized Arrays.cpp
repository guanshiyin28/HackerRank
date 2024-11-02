#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q;
cin >> n >> q;

vector<vector<int>> a(n);

for (int i=0; i < n; i++){
    int k;
    cin >> k;
    a[i].resize(k);

    for (int j=0; j < k; j++){
        cin >> a[i][j];
    }
}

for (int i=0; i < q; i++){
    int index, j;
    cin >> index >> j;
    cout << a[index][j]<< endl;
}
return 0;

}
