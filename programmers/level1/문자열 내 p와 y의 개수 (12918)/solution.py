def solution(s):
    answer = True
    a = s.upper()
    if (a.count('P')==a.count('Y')):
        answer = True
    else:
        answer = False
    return answer