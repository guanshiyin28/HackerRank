#include <iostream>
#include <string>
using namespace std;

int main() { string a="abcd"; string b="ef";

cout<<a.length()<<" "<<b.length()<<endl;

string temp=a+b;
cout<<temp<<endl;

swap(a[0],b[0]);
cout<<a<<" "<<b;

return 0;

}
