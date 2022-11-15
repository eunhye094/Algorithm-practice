def solution(hp):
    # answer = 0
    # for i in [5, 3, 1]:
    #     answer+=hp//i
    #     hp%=i
    # return answer
    return hp//5 + (hp%5)//3 + (hp%5)%3