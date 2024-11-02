# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = list(map(int, input().split())), list(map(int, input().split()))

l = [(x, y) for x in a for y in b]

print(*l)
