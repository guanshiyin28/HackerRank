import numpy

def arrays(arr):
    l = arr[::-1]
    a = numpy.array(l, float)
    return a 

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
