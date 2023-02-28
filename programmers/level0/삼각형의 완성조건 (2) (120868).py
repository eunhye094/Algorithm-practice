def solution(sides):
    # return len(range(max(sides), sum(sides))) + len(range(max(sides)-min(sides)+1, max(sides)))
    # return sum(sides) - max(sides) + min(sides) - 1
    return min(sides)*2-1