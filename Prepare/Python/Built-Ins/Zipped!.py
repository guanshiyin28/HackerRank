# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
print(*map(lambda i: sum(i)/len(i), zip(*[list(map(float, input().split()))[:n] for _ in range(x)])), sep='\n')
