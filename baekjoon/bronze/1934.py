def gcd(a,b):
    while(b!=0):
        a, b = b, a%b
    return int(a)
def lcm(a,b):
    return int((a*b)/gcd(a,b))

cnt = int(input())

for _ in range(cnt):
    a, b = map(int, input().split())
    print(lcm(a,b)) if a>=b else print(lcm(b,a))