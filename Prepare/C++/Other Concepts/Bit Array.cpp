#include <iostream>


int main() {
    static_assert(sizeof(unsigned int) == 4);
    unsigned int N, S, P, Q;
    
    std::cin >> N >> S >> P >> Q;
    
    auto count =0;
    auto previous = S;
    while (N--) {
        auto brandnew = previous * P + Q;
        if (brandnew != previous) ++count;
        previous = brandnew;
    }
       
    std::cout << count;
    return 0;
}
