# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
orders = OrderedDict()
for i in range(int(input())):
    name, _, price = input().rpartition(' ')
    orders[name] = orders.get(name, 0) + int(price)
[print(*item) for item in orders.items()]
