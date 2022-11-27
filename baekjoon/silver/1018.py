import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
result = []
check = [['W', 'B'], ['B', 'W']]    #[합이 짝, 합이 홀]

for _ in range(n):
    board.append(list(input()))

for x in range(n-7):
    for y in range(m-7):
        cnt = [0, 0]
        for i in range(x, x+8):
            for j in range(y, y+8):
                if board[i][j]!=check[0][(i+j)%2]:
                    cnt[0]+=1
                if board[i][j]!=check[1][(i+j)%2]:
                    cnt[1]+=1
        result.append(cnt[0])
        result.append(cnt[1])

print(min(result))