def average(array):
    # your code goes here
    x = set(arr)
    return f'{(sum(x) / len(x)):.3f}'

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
