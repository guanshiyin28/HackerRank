# Enter your code here. Read input from STDIN. Print output to STDOUT
def isaFloat(string):
    try:
        if string == '0':
            return False
        float(string.strip())
        return True
    except ValueError:
        return False
        
for nums in range(int(input())):
    print(isaFloat(input()))
