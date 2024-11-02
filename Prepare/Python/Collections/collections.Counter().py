# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

number_of_shoes = int(input())
shoe_sizes = list(input().split())
number_of_customers = int(input())

shoe_sizes = Counter(shoe_sizes)
total = 0

for customers in range(number_of_customers):
    
    size, price = map(int, input().split())

    if shoe_sizes[str(size)]:
        shoe_sizes[str(size)] -= 1
        total += price

print(total)
