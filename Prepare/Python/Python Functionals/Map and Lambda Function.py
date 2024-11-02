cube = lambda x: x**3

def fibonacci(n):
    res = [0, 1]
    for i in range(2, n):
        res.append(res[i - 1] + res[i - 2])
    return res[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
