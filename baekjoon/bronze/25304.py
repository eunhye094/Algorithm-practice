total = int(input())
count = int(input())
for i in range(count):
    thing=input().split()
    total-=int(thing[0])*int(thing[1])
print("Yes") if total==0 else print("No")
