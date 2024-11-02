# Enter your code here. Read input from STDIN. Print output to STDOUT
print((lambda a, b, c, d: (a**b) + (c**d))(*[int(input()) for _ in range(4)]))
