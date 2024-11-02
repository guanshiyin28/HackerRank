import numpy

a , b = map(int,input().split())


arrayList = []
for i in range(a):
    arrayList.append(list(map(int,input().split())))


my_array = numpy.array(arrayList)
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None), 11))
