def solution(num, k):
    # ans = str(num).find(str(k))
    # return ans+1 if ans!=-1 else ans
    return str(num).find(str(k))+1 if str(k) in str(num) else -1