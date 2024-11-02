for i in range(1,int(input())+1):
    print(sum(map(lambda x: x[1]**x[0], enumerate([10]*i)))**2)
