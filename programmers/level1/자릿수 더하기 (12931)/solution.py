def solution(n):
    answer = 0
    for i in range(len((str(n)))):
        answer+=int(n%10)
        n/=10
    return answer