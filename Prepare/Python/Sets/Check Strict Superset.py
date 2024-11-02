# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
print(all([a.issuperset(set(map(int, input().split()))) for _ in range(int(input()))]))
