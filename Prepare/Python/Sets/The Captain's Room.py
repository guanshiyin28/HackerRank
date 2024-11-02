# Enter your code here. Read input from STDIN. Print output to STDOUT
k, t = int(input()), list(map(int, input().split()))
print(((sum(set(t))*k)-sum(t))//(k-1))
