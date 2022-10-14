n = int(input())

if(n<=1):
    print(1)
else:
    fac = 1
    for i in range(2, n+1):
        fac*=i
    print(fac)