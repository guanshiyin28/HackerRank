# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nE = set(map(int, input().split()))

b = int(input())
bF = set(map(int, input().split()))

print(len(nE | bF))
