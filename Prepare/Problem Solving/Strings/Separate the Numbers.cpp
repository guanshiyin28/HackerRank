#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

void separateNumbers(string s) {
    int bl = 1;
    bool f = false;
    while(bl * 2 <= s.size()){
        string base = s.substr(0, bl);
        string newString = "";
        long baselong = atol(base.c_str());
        do{
            newString += to_string(baselong);
            baselong++;
        }while(newString.size() < s.size());
        if(newString == s) {cout << "YES " << base;f = true;break;}
        bl++;
    }
    if(!f) cout << "NO";
    cout << endl;
}

int main()
{
    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s;
        getline(cin, s);

        separateNumbers(s);
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
