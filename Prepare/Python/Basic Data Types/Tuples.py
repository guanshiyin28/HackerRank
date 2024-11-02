#Try in PYPY3
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    b=tuple(integer_list)
    print(hash(b))
