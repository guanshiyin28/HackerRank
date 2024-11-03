#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    //taking input
    int n{};
    cin >> n;
    vector<int> v;
    for (int i{0}; i < n; ++i)
    {
        int t{};
        cin >> t;
        v.push_back(t);
    }
    // s is number of queries
    int s;
    cin >> s;
    // foreach query, get the value and print necessary value
    for (int i{0}; i < s; ++i)
    {
        int num{}; cin >> num;
        // lower bound returns an iterator type variable
        vector<int>::iterator x;
        x = lower_bound(v.begin(), v.end(), num);
        // getting the index of the lowerbound in the vector
        int pos = x - v.begin(); 
        // if value of lb = the query num, then yes it exists
        // in the vector exists
        if (v[pos] == num) cout << "Yes "<< pos+1;
        else cout << "No "<< pos+1;
        cout << endl;
    }
    
    return 0;
}
