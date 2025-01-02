#include <bits/stdc++.h>

using namespace std;

int marsExploration(string s) {
   int result = 0;
    string base = "SOS";
    for(int i = 0; i < s.size(); i++) if(s[i] != base[i%3]) result++;
    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = marsExploration(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
