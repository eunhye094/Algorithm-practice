def solution(keyinput, board):
    ans = [0, 0]
    for i in keyinput:
        if i=='up' and ans[1]<board[1]//2:
            ans[1]+=1
        elif i=='down' and ans[1]>-1*(board[1]//2):
            ans[1]-=1
        elif i=='left' and ans[0]>-1*(board[0]//2):
            ans[0]-=1
        elif i=='right' and ans[0]<board[0]//2:
            ans[0]+=1
    return ans