import fractions

def solution(a, b):
    c = fractions.Fraction(a, b)
    x = c.denominator
    
    while x%2==0:
        x//=2
    while x%5==0:
        x//=5
        
    if x==1:
        return 1
    else:
        return 2
    
    #내 방법: 직접 소인수분해하고 set([소인수목록])&set([2, 5])==set([소인수목록]) 확인