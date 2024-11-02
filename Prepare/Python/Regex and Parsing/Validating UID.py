# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    s = input()
    m = re.search(r'^(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})[A-Za-z0-9]{10}$', s)
    if m and len(s)==len(set(s)):
        print("Valid")
    else:
        print("Invalid")
