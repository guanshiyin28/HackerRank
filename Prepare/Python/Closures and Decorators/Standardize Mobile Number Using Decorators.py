from re import sub
def wrapper(f):
    def fun(l):
        return f([sub(r"(.*){0,3}(\d{5})(\d{5})$",\
        r"+91 \2 \3", num)for num in l])
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


