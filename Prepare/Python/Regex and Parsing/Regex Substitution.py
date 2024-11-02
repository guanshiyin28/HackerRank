# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
text = [input() for x in range(n)]
pattern1 = re.compile(r'(?<= )&&(?= )')
pattern2 = re.compile(r'(?<= )\|\|(?= )')

for x in text:
    x = (re.sub(pattern1, "and", x))
    x = (re.sub(pattern2, "or", x))

    print(x)
