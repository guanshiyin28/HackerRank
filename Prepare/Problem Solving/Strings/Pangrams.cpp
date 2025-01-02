#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    getline(cin, s);
    vector<int> c(26, 0);
    for(int i = 0; i < s.size(); i++){
        if(s[i] != ' ')
        c[tolower(s[i]) - 'a']++;
    }
    string r = "pangram";
    for(int i = 0; i < c.size(); i++){
        if(c[i] == 0){
            r = "not " + r;
            break;
        }
    }
    cout << r ;
    return 0;
}
