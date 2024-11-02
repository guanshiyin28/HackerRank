# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

pattern = re.compile(r'^[4-6](\d{3})-?(\d{4})-?(\d{4})-?(\d{4})$')
pattern_duplicate = re.compile(r'(\d)\1{3}')

for x in range(n):
    card = input()
    if bool(pattern.match(card)):
        valid_card = re.sub(r'-', "", card)
        if not bool(pattern_duplicate.search(valid_card)):
            print("Valid")
        else:
            print("Invalid")
        
    else:
        print("Invalid")
