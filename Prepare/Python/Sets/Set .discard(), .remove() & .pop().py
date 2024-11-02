n = int(input())
s = set(map(int, input().split()))
cn = int(input())

for i in range(cn):
    command, *number = input().split()
    
    if number:
        number = int(number[0])
        eval(f"s.{command}(number)")
    
    else:
        eval(f"s.{command}()")

print(sum(s))
