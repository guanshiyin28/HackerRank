# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

com = complex(input())

r, phi = cmath.polar(com)
print(f"{r}\n{phi}")
