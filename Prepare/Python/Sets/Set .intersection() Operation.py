# Enter your code here. Read input from STDIN. Print output to STDOUT
el = int(input())
e = set(list(map(int, input().split()))[:el])
fl = int(input())
f = set(list(map(int, input().split()))[:fl])
print(len(e.intersection(f)))
