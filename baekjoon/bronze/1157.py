s = input().upper()
s2 = list(set(s))
cnt = []

for x in s2:
    cnt.append(s.count(x))

if cnt.count(max(cnt))>1:
    print("?")
else:
    print(s2[cnt.index(max(cnt))])