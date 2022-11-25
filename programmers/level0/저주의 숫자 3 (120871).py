def solution(n):
    ans = 0
    # num = 0
    # while num<n:
    #     ans+=1
    #     if ans%3!=0 and '3' not in str(ans):
    #         num+=1
    for _ in range(n):
        ans+=1
        while ans%3==0 or '3' in str(ans):
            ans+=1
    return ans