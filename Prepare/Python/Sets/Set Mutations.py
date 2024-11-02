# Enter your code here. Read input from STDIN. Print output to STDOUT
al = int(input())
a = set(list(map(int, input().split()))[:al])
for _ in range(int(input())):
    c, l = input().split()
    if not hasattr(set, c):
        continue
    getattr(a, c)(set(list(map(int, input().split()))[:int(l)]))
print(sum(a))
