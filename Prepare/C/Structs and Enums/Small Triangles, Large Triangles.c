#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;


double squart(triangle triangle)
{
    double p = (triangle.a + triangle.b + triangle.c) / 2.0;
    double s = sqrt((double)(p * (p - triangle.a) * (p - triangle.b) * (p - triangle.c)));
    return s;
}
void sort_by_area(triangle* tr, int n) {
    /**
    * Sort an array a of the length n
    */
    int tap = n / 2;
    for(tap; tap > 0; tap /= 2)
    {
        for(int i = tap; i < n; i++)
        {
            for(int j = i - tap; j >= 0 && squart(tr[j]) > squart(tr[j+tap]); j -= tap)
            {   
                triangle temp = tr[j];
                tr[j] = tr[j+tap];
                tr[j+tap] = temp;
            }
        }
    }
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
