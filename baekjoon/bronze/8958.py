'''
for i in range(int(input())):
    ox = input()
    total = 0
    score = 1
    for j in ox:
        if(j=='X'):
            score=1
        else:
            total+=score
            score+=1
    print(total)
'''

for i in range(int(input())):
    oList = input().split('X')
    score = 0
    for i in oList:
        score+=sum(range(1, len(i)+1))
    print(score)