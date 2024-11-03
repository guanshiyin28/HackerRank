#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Matrix {
public:
    vector<vector<int>> a;

    Matrix operator+(const Matrix& b) {
    Matrix m;
    m.a.resize(b.a.size());
        for (int i = 0; i < a.size(); i++) {
            m.a[i].resize(b.a[i].size());
        }

    for (int i = 0; i < b.a.size(); i++) {
        for (int j = 0; j < b.a[i].size(); j++) {
            m.a[i][j] = a[i][j] + b.a[i][j];
        }
    }
    return m;
}
};


int main () {
   int cases,k;
   cin >> cases;
   for(k=0;k<cases;k++) {
      Matrix x;
      Matrix y;
      Matrix result;
      int n,m,i,j;
      cin >> n >> m;
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         x.a.push_back(b);
      }
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         y.a.push_back(b);
      }
      result = x+y;
      for(i=0;i<n;i++) {
         for(j=0;j<m;j++) {
            cout << result.a[i][j] << " ";
         }
         cout << endl;
      }
   }  
   return 0;
}
