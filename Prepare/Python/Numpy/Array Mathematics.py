import numpy as np

n, m = map(int, input().split())

arrays = [] # contains all the inputs for compute

try :
    while True:
        arr = input()
        if not arr:
            break
        arrays.append(list(map(int, arr.split())))
except EOFError:
    pass

# handles both 2d and 1d arrays
if n == 1:
    a = np.array(arrays[0])
    b = np.array(arrays[1])
else: 
    a = np.array(arrays[:2]).reshape(n, m)
    b = np.array(arrays[2:]).reshape(n, m)

actions = ["add", "subtract", "multiply", "floor_divide", "mod", "power"]

for action in actions:
    result = getattr(np, action)(a, b)
    if n == 1:
        print(f"[{result}]")
    else:
        print(f"{result}") 
