import numpy
matrices = []
n = int(input())
for i in range(2):
    matrix = []
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    matrices.append(matrix)
print(numpy.dot(matrices[0],matrices[1]))
