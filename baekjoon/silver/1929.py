import math

def is_prime_num(a):
    if(a==1):
        return False
    else:
        for i in range(2, int(math.sqrt(a))+1):
            if(a%i==0):
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if(is_prime_num(i)):
        print(i)