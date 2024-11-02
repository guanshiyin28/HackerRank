def has_vowel(letters):
    v_sum =sum([['a', 'e', 'i', 'o', 'u', 'y'].count(l) for l in letters]) 
    return  2 if  v_sum %2 == 0 else 1    
def score_words(words):
    return sum([has_vowel(w) for w in [[*map(str,word)] for word in words]])


n = int(input())
words = input().split()
print(score_words(words))
