# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())

student = namedtuple("Student", input().split())

total = 0

for i in range(n):
    ll = input().split()
    st = student(*ll)
    total += int(st.MARKS)

average = total / n
print(f"{average:.2f}")
