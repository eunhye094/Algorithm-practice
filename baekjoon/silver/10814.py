member = []

for _ in range(int(input())):
    age, name = input().split()
    member.append([int(age), name])

member.sort(key=lambda x: x[0])

for m in member:
    print(m[0], m[1])