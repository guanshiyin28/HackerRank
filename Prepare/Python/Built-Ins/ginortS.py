# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string=input()
lc=re.findall(r'[a-z]',string)
uc=re.findall(r'[A-Z]',string)
num=re.findall(r'[0-9]',string)
od=[ i for i in num if int(i)%2!=0]
ev=[ i for i in num if int(i)%2==0]
print(*sorted(lc),*sorted(uc),*sorted(od),*sorted(ev),sep="")
