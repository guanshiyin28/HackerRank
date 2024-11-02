def mutate_string(string, position, character):
    mutate=""
    i=0
    while i<position:
        mutate+=string[i]
        i+=1
    mutate+=character
    mutate+=string[i+1:]
    return mutate

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
