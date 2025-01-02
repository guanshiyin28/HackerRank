#include <bits/stdc++.h>

using namespace std;

int camelcase(string s) {
    int cnt = 1;
    for (int i : s) {
        if (isupper(i)) {
            cnt++;
        }
    }
    return cnt;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = camelcase(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
