#include <iostream>
#include <cstdio>
using namespace std;

int main() { int i; long l; char c; double d; float f;

scanf("%d %ld %c %f %lf", &i, &l, &c, &f, &d);
printf("%d\n%ld\n%c\n%0.3f\n%0.9lf\n", i, l, c, f, d);
return 0;

}
