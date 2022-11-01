import sys
input=sys.stdin.readline

iron=input()
stack=[]
cnt=0

#참고한 풀이
for i in range(len(iron)):
    if iron[i]==')':
        stack.pop()
        if iron[i-1]=='(':  #바로 닫으면 레이저
            cnt+=len(stack)
        else:   #아니면 쇠막대기
            cnt+=1
    else:
        stack.append(iron[i])

#내가 짠 풀이
# for i in range(len(iron)):
#     if iron[i]==')':
#         if i-stack.pop()[0]==1:
#             cnt+=len(stack)
#         else:
#             cnt+=1
#     else:
#         stack.append([i, iron[i]])

print(cnt)