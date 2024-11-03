#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int Q;
    cin >> Q;

    set<int> s;

    for (int i = 0; i < Q; i++) {
        int queryType, queryValue;
        cin >> queryType >> queryValue;

        if (queryType == 1) {
            s.insert(queryValue);
        } else if (queryType == 2) {
            s.erase(queryValue);
        } else if (queryType == 3) {
            set<int>::iterator it = s.find(queryValue);
            if (it != s.end()) {
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        }
    }

    return 0;
}
