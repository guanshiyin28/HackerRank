#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int i = 1;
    while(i < s.size()){
        if(s[i-1] == s[i]){
            s.erase(i-1, 2);
            if( i != 1) i--;
        }
        else i++;
    }
    if(s == "") s = "Empty String";
    cout << s;
    return 0;
}
