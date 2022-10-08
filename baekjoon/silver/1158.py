n, k = map(int, input().split())
target = 0
people = [i for i in range(1, n+1)]
result = []

while(people):
    target+=(k-1)
    if(target>=len(people)):
        target = target%(len(people))
    result.append(str(people.pop(target)))

print('<'+', '.join(result)+'>')