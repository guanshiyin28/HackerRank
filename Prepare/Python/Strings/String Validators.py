if __name__ == '__main__':
    s = input()
    for func_name in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any(eval(f'char.{func_name}()') for char in s))
