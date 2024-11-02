def runner_up(arr):
    max_ = max(arr)  # Gets the first max element
    arr = [x for x in arr if x != max_]  
    max2 = max(arr)  # Gets the second max element
    return max2

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  
    print(runner_up(arr))
