def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer

# def solution(n):
#     prime = [False, False, True]+[True for i in range(n-2)]
#     answer = []
    
#     for i in range(2, int(n**0.5)+1):
#         if prime[i]:
#             for j in range(2*i, n+1, i):
#                 prime[j]=False
    
#     for i in range(n+1):
#         if prime[i] and n%i==0:
#             answer.append(i)

#     return answer