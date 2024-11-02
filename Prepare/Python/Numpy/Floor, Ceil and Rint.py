import numpy as np
np.set_printoptions(legacy='1.13')

actions = ["floor", "ceil", "rint"]

a = list(map(float, input().split()))

for action in actions:
    result = getattr(np, action)(a)
    print(result)
