def solution(order):
    # answer = 0
    # for i in str(order):
    #     if i=='3' or i=='6' or i=='9':
    #         answer+=1    
    # return answer
    return str(order).count('3') + str(order).count('6') + str(order).count('9')