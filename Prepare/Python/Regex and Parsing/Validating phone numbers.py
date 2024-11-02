# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = r'^[789]\d{9}$'
for _ in range(int(input())):
    print("YES" if re.match(p, input()) else "NO")
