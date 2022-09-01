def solution(n):
    a = ['수', '박']
    answer = ''
    for i in range(n):
        answer += a[i%2]
    return answer