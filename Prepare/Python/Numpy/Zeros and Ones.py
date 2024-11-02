import numpy

shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, numpy.int8))
print(numpy.ones(shape, numpy.int8))
