import numpy

a , b = map(int,input().split())

arrayList = []
for i in range(a):
    arrayList.append(list(map(int,input().split())))

print(numpy.max(numpy.min(arrayList, axis = 1)))
