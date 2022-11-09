import math

def solution(n):
    return n/math.gcd(n, 6)
    #return n*6/math.gcd(n, 6)/6