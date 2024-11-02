#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int next_permutation(int n, char **s)
{
	 // Step 1: Find the largest index k such that s[k] < s[k + 1]
    int k = -1;
    for (int i = 0; i < n - 1; i++) {
        if (strcmp(s[i], s[i + 1]) < 0) {
            k = i;
        }
    }
    if (k == -1) {
        return 0; // No next permutation
    }

    // Step 2: Find the largest index l greater than k such that s[k] < s[l]
    int l = -1;
    for (int i = k + 1; i < n; i++) {
        if (strcmp(s[k], s[i]) < 0) {
            l = i;
        }
    }

    // Step 3: Swap the value of s[k] with that of s[l]
    char *temp = s[k];
    s[k] = s[l];
    s[l] = temp;

    // Step 4: Reverse the sequence from s[k + 1] to s[n - 1]
    for (int i = k + 1, j = n - 1; i < j; i++, j--) {
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }

    return 1; // Next permutation exists
}

int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}
