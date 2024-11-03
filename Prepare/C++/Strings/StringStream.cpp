#include <sstream>
#include <vector>
#include <iostream>
using namespace std; int main() {

string input{};
cin >> input;
stringstream ss(input);

vector<int> nums{};
int n{};
char bin{};
int check{};
if (!((ss.peek() - 48 > -1 && ss.peek() - 48 < 10) || ss.peek() == 45)) {
    ss >> bin;
}
while ((ss.peek() - 48 > -1 && ss.peek() - 48 < 10) || ss.peek() == 45)
{
    check = ss.peek() - 48;
    if((check > -1 && check < 10)|| check == -3){
        ss >> n;
        nums.push_back(n);
    }

    ss >> bin;
}

for (int n : nums)
{
    cout << n << '\n';
}
return 0;

}
