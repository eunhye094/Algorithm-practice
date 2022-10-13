#문제 3. 출석부

n, k = map(int, input().split())
attendance = []

for i in range(n):
	name, height = input().split()
	attendance.append({'name': name, 'height': height})

attendance.sort(key=(lambda x: (x['name'], x['height'])))
print(attendance[k-1]['name'], attendance[k-1]['height'])