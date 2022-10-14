n, m = map(int, input().split())

def cnt_num(x, n):
    cnt=0
    while(x>=n):
        cnt+=x//n
        x//=n
    return cnt

cnt2 = cnt_num(n, 2) - cnt_num(m, 2) - cnt_num(n-m, 2)
cnt5 = cnt_num(n, 5) - cnt_num(m, 5) - cnt_num(n-m, 5)

print(min(cnt2, cnt5))