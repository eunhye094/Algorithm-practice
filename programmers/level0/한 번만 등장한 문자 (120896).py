def solution(s):
    # cnt={}
    # for i in s:
    #     if cnt.get(i):
    #         cnt[i]+=1
    #     else:
    #         cnt[i]=1
    # return ''.join(sorted([i for i in cnt.keys() if cnt[i]==1]))
    return ''.join(sorted([i for i in s if s.count(i)==1]))