# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stamps = [input() for i in range(n)]

distinct_country = set()
for i in stamps:
    distinct_country.add(i)

print(len(distinct_country))
