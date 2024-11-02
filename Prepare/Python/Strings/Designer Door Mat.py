dimension = input().split()
N = int(dimension[0])
M = int(dimension[1])

for i in range(1,N+1):
    if i == int(N/2+0.5):
        print("WELCOME".center(M, "-"))
    elif i < int(N/2+0.5):
        stringa = ".|."*(i-1)+".|."+".|."*(i-1)
        if M >= len(stringa):
            print(stringa.center(M, "-"))
        else: stringa
    elif i > int(N/2+0.5):
        stringa = ".|."*(N-i)+".|."+".|."*(N-i)
        if M >= len(stringa):
            print(stringa.center(M, "-"))
        else: stringa
