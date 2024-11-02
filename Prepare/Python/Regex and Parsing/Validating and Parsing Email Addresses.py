# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import email.utils
p = r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
for _ in range(int(input())):
    n, e = email.utils.parseaddr(input())
    if re.match(p, e):
        print(email.utils.formataddr((n, e)))
