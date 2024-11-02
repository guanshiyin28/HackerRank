# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    n = int(input())
    cubelist = list(map(int, input().split()))
    stackable = True
    for i in range(1, n-1):
        if cubelist[i-1] < cubelist[i] and cubelist[i] > cubelist[i+1]:
            stackable = False
            break
    if stackable:
        print("Yes")
    else:
        print("No")
