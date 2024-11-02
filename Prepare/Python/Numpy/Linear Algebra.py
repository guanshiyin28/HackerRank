from numpy import linalg
print(round(linalg.det([list(map(float, input().split())) for _ in range(int(input()))]), 2))
