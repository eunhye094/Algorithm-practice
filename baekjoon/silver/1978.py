import math

def is_prime_num(a):
    if a<=1:
        return False
    else:
        for i in range(2, int(math.sqrt(a))+1):
            if(a%i==0):
                return False
        return True

cnt = int(input())
num = map(int, input().split())
prime = 0

for i in num:
    if is_prime_num(i):
        prime+=1

print(prime)
