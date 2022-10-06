#문제 2. 동명이인

stuNum, target = input().split()
cnt = 0
for _ in range(int(stuNum)):
	stu = input()
	if target in stu:
		cnt+=1
print(cnt)