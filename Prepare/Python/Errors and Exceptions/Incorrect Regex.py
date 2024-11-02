# Enter your code here. Read input from STDIN. Print output to STDOUT
#In Python 3, it will not work; but it will work in Pypy 3
import re 
T =int(input())
for x in range(T):
    S = input()
    try:
        if re.compile(S):
            print("True")
    except:
        print("False")
