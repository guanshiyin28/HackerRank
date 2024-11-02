# Enter your code here. Read input from STDIN. Print output to STDOUT
print(*(lambda a,b,m : (pow(a, b), pow(a, b, m)))(*[int(input()) for _ in range(3)]), sep='\n')
