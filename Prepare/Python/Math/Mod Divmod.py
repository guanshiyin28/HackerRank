# Enter your code here. Read input from STDIN. Print output to STDOUT
import os

a = int(input())
b = int(input())

print(a//b, a%b, divmod(a,b), sep=os.linesep)
