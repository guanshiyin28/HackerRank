# Enter your code here. Read input from STDIN. Print output to STDOUT
from re import findall, IGNORECASE
print('\n'.join(findall(r'(?=[^aeiou]([aeiou]{2,})[^aeiou])', input(), IGNORECASE)) or -1)
