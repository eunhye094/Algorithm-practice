def solution(n):
    #return int(''.join(str(j) for j in (sorted([int(i) for i in str(n)], reverse=True))))
    return int(''.join((sorted(list(str(n)),reverse=True))))