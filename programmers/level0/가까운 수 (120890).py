def solution(array, n):
    # answer = 0
    # tmp = n + 100
    # array.sort()
    # for i in array:
    #     if abs(n-i)<tmp:
    #         answer = i
    #         tmp = abs(n-i)
    # return answer
    return sorted(array, key=lambda x: (abs(x-n), x))[0]
