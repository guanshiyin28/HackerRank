# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
if __name__ == '__main__':
    contain = list(map(int, input().split(' ')))
    alist = list(map(str, input().split(' ')))
    a = set(map(str, input().split(' ')))
    b = set(map(str, input().split(' ')))
    fs = collections.Counter(alist)
    ha = 0
    hb = 0
    for c in a:
        if c in fs.keys():
            ha = ha+ int(fs[c])
    for c in b:
        if c in fs.keys():
            hb = hb + int(fs[c])
    print(ha-hb)
