# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p1 = r'{[^{}]*}'
p2 = r'#[\da-fA-F]{3,6}'
t = ''.join(input() for _ in range(int(input())))
t = ''.join(re.findall(p1, t))
print('\n'.join(re.findall(p2, t)))
