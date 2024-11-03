#include <iostream>
#include <string>
using namespace std;

int main() {
    // Complete the program
    string letras_a;
    string letras_b;
    cin >> letras_a;
    cin >> letras_b;
    
    cout << letras_a.size() <<" ";
    cout << letras_b.size() << endl;
    
    cout << letras_a + letras_b << endl;
    cout << letras_b[0];
    for(int i = 1;i<letras_a.size();i++){
        cout << letras_a[i];
    }
    cout << " " << letras_a[0];
    for(int i = 1;i<letras_b.size();i++){
        cout << letras_b[i];
    }
    
    return 0;
}
