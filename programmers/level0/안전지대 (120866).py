def solution(board):
    n = len(board[0])
    a = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y]==1:
                for i in range(1, -2, -1):
                    for j in range(1, -2, -1):
                        if 0<=x+i<n and 0<=y+j<n:
                            a[x+i][y+j]=1
    return sum(a, []).count(0)