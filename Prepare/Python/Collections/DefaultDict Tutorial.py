# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())

### Optimized Version ###
# Precompute the positions of each value in group_A
positions_dict = defaultdict(list)
for i in range(n):
    value = input()
    positions_dict[value].append(i + 1)  # Store 1-based index positions

# Check and print the positions for each value in group_B
for _ in range(m):
    value = input()
    if value in positions_dict:
        print(*positions_dict[value])  # Print all positions found
    else:
        print(-1)  # Print -1 if no occurrence found

### Less Efficient Version ###
# for _ in range(n):
#     d['group_A'].append(input())
# for _ in range(m):
#     d['group_B'].append(input())
    
# for value in d['group_B']:
#     positions = [i + 1 for i, v in enumerate(d['group_A']) if v == value]  # Find all occurrences
#     if positions:
#         print(*positions)  # Print all positions found
#     else:
#         print(-1)  # Print -1 if no occurrence found
