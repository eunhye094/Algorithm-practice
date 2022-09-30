cnt = int(input())

# stack 사용
for _ in range(cnt):
    word = input().split()
    for i in word:
        stack = list(i)
        while(stack):
            print(stack.pop(), end='')
        print(" ", end='')
    print("")

# slicing 사용
# for _ in range(cnt):
#     word = input().split()
#     for i in word:
#         print(i[::-1], end=" ")
#     print("")