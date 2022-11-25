# def solution(score):
#     s = sorted(score, reverse=True, key=sum)
#     s2 = [1]
    
#     for i in range(1, len(s)):
#         if sum(s[i-1])==sum(s[i]):
#             s2.append(s2[i-1])
#         else:
#             s2.append(i+1)

#     return [s2[s.index(x)] for x in score]

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]   #index는 동일한 것 중에 가장 앞 index 반환
