def is_leap(year):
    leap = False
    
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True

    
    return leap

year = int(input())
print(is_leap(year))
