# Enter your code here. Read input from STDIN. Print output to STDOUT
N, A = int(input()), input().split()
print(all(int(x)>0 for x in A) and any(x == x[::-1] for x in A))
