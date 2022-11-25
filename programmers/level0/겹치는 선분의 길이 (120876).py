# from collections import defaultdict
# def solution(lines):
#     line = defaultdict(int)
#     for i in lines:
#         for j in range(i[0], i[1]):
#             line[j]+=1
#     return len(line)-list(line.values()).count(1)

def solution(lines):
    sets = [set(range(l[0], l[1])) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])