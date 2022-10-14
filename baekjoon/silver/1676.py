n = int(input())
cnt = 0

while(n>=5):
    cnt += n//5
    n //= 5

print(cnt)

# n = int(input())
# result = 1
# cnt = 0

# if(n>1):
#     for i in range(2, n+1):
#         result*=i

# for i in range(len(str(result))-1, 0, -1):
#     if(str(result)[i]=='0'):
#         cnt+=1
#     else:
#         break

# print(cnt)