def solution(polynomial):
    ans=[0, 0]
    for p in polynomial.split(' + '):
        if 'x' in p:
            if p=='x': ans[0]+=1
            else: ans[0]+=int(p[:-1])
        else:
            ans[1]+=int(p)
            
    if ans[0]==0 and ans[1]==0:
        return '0'
    elif ans[0]==0:
        return str(ans[1])
    elif ans[0]==1:
        if ans[1]==0:
            return 'x'
        else:
            return 'x + '+str(ans[1])
    else:
        if ans[1]==0:
            return str(ans[0])+ 'x'
        else:
            return str(ans[0])+ 'x + ' + str(ans[1])