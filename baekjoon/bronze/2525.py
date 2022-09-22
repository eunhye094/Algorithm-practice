hour, min = map(int, input().split())
min += int(input())

while(min>=60):
    hour+=1
    min-=60
while(hour>=24):
    hour-=24

print(hour, min)