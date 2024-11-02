# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = {}

for i in range(n):    
    key = input()
    if key in words:
        words[key] += 1
    else:
        words[key] = 1

print(len(words))
print(*words.values())
