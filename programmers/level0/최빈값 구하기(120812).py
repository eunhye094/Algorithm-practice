def solution(array):
    num = {}
    for i in array:
        if num.get(i):
            num[i]+=1
        else:
            num[i]=1
    ans = sorted(num.keys(), reverse=True, key=lambda x: num[x])
    return -1 if len(ans)>1 and num[ans[0]]==num[ans[1]] else ans[0]
