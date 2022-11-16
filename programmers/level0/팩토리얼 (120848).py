def solution(n):
    answer = 1
    fac = 1
    while n>=fac:
        answer+=1
        fac*=answer
    return answer-1