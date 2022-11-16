def solution(num_list, n):
    # answer = []
    # for i in range(0, len(num_list), n):
    #     answer.append(num_list[i:i+n])
    # return answer
    return [[num_list[i*n+j] for j in range(n)] for i in range(len(num_list)//n)]