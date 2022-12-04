import sys
input = sys.stdin.readline

n = int(input())    #최대 8개 → 전체 확인 가능
egg = [list(map(int, input().split())) for _ in range(n)]

def hit(idx):
    #깰 계란이 없으면 종료
    if idx==n:
        cnt=0
        for s, w in egg:
            if s <= 0:
                cnt += 1
        return cnt
    
    #현재 손에 든 계란 깨짐
    if egg[idx][0]<=0:
        return hit(idx+1)

    #안 깨진 계란 남아있는지 확인
    for i in range(n):
        if i == idx:
            continue
        if egg[i][0] > 0:
            break
    else:
        return hit(idx+1)

    #시뮬레이션
    ans=0
    for i in range(n):
        if i == idx:
            continue
        if egg[i][0]<=0:
            continue

        egg[idx][0]-=egg[i][1]
        egg[i][0]-=egg[idx][1]

        ans=max(ans, hit(idx+1))

        #다음 단계로 가기 위해 다시 초기화
        egg[idx][0]+=egg[i][1]
        egg[i][0]+=egg[idx][1]

    return ans

print(hit(0))