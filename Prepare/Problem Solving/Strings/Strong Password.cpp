#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

char getNature(char c){
    if(c >= '0' && c <='9') return 'n';
    if(c >= 'a' && c <= 'z') return 'l';
    if(c >= 'A' && c <= 'Z') return 'u';
    return 's';
}

int minimumNumber(int n, string password) {
    map<char, int> mp;
    for(char c: password){
        mp[getNature(c)] = 1;
    }
    return max(4 - (int)mp.size(), 6 - n); 
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string password;
    getline(cin, password);

    int answer = minimumNumber(n, password);

    fout << answer << "\n";

    fout.close();

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
