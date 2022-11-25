# from itertools import permutations

# def solution(babbling):
#     answer = 0
#     words = []
#     for i in range(4):
#         words+=[''.join(p) for p in list(permutations(["aya", "ye", "woo", "ma"], i+1))]
#     for b in babbling:
#         if b in words:
#             answer+=1
#     return answer

def solution(babbling):
    ans = 0
    for b in babbling:
        for w in ["aya", "ye", "woo", "ma"]:
            b = b.replace(w, ' ')    #yayae 방지
        if len(b.strip()) == 0:     #공백 제거
            ans+=1
    return ans