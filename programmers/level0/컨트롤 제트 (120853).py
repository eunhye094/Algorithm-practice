def solution(s):
    tmp=[]
    for i in s.split():
        if i=='Z' and tmp:
            tmp.pop()
        else:
            tmp.append(int(i))
    return sum(tmp)