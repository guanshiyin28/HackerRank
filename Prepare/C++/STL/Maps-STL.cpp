#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int q_no, q_type, marks;
    string name;
    map<string, int> m;
    map<string, int>::iterator it;
    
    cin >> q_no;
    
    while(q_no){
        cin >> q_type;
        switch(q_type){
            case 1:
                cin >> name >> marks;
                it = m.find(name);
                if(it != m.end()){
                    m[name] += marks;
                }
                else{
                    m.insert(make_pair(name, marks));    
                }               
                break;
            case 2:
                cin >> name;
                m[name] = 0;
                break;
            case 3:
                cin >> name;
                it = m.find(name);
                (it != m.end()) ? cout<< m[name] << endl : cout<< 0 << endl;
                break;
        }
        
        q_no--;
    }
    
    return 0;
}
