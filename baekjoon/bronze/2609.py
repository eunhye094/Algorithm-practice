def gcd(a, b):
    while(b!=0):
        a, b = b, a%b
    return int(a)

def lcm(a, b):
    return int((a*b)/gcd(a,b))

a, b = map(int, input().split())

print(gcd(a,b)) if a>=b else print(gcd(b,a))
print(lcm(a,b))

# import math

# print(math.gcd(a,b))
# print(math.lcm(a,b))
