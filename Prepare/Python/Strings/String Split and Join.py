def split_and_join(line):
    line=('-'.join(line.split(" ")))
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
