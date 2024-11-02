def merge_the_tools(string, k):
    # your code goes here
    # parts = [string[i:i+ k] for v, i in enumerate(range(0, len(string), k))]
    parts = [string[i:i + k] for i in range(0, len(string), k)]

    for item in parts:
        unique_items = ''.join(sorted(set(item), key=item.index))
        print(unique_items)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
