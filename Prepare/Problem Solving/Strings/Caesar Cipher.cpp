#include <bits/stdc++.h>
using namespace std;
int main()
{
   string s;
   int cipher;
   cin >> cipher;
   cin >> s;
   cin >> cipher;
   for(char &c:s) {
       if(isalpha(c)){
           char a = isupper(c)? 'A':'a';
           c = a + (c - a + cipher) % 26;
       }
   }
    cout << s ;
    return 0;
}
