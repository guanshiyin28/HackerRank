# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    al = int(input())
    a = set(list(map(int, input().split()))[:al])
    bl = int(input())
    b = set(list(map(int, input().split()))[:bl])
    print(a.issubset(b))
