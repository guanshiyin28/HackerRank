#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

int validSize(string s, char first, char second){
    string ans = "";
    for(int i = 0; i < s.size(); i++){
        if(s[i] == first || s[i] == second){
            if(ans.size() > 0 && ans[ans.size() - 1] == s[i]) return 0;
            else ans+=s[i];
        }
    }
    if(ans.size() < 2) return 0;
    return ans.size();
}

int alternate(string s) {
    int ans = 0;
    for(char i = 'a'; i < 'z'; i++){
        for(char j = i + 1; j <= 'z'; j++){
           int r = validSize(s, i, j);
           if(r > ans) ans = r;
        }
    }
    return ans;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string l_temp;
    getline(cin, l_temp);

    int l = stoi(ltrim(rtrim(l_temp)));

    string s;
    getline(cin, s);

    int result = alternate(s);

    fout << result << "\n";

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
