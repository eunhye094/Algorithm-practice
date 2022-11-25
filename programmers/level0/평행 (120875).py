def solution(dots):
    #평행 조건 = 기울기가 같을 것 (y변화량/x변화량)
    lean = []
    for i in range(4):
        for j in range(i+1, 4):
            t = (dots[i][1]-dots[j][1])/(dots[i][0]-dots[j][0])
            if t in lean:
                return 1
            lean.append(t)
    return 0