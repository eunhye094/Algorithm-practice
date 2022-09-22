num = int(input())
new = num
count = 0

while True:
    a = new//10
    b = new%10
    c = a+b
    new = b*10 + c%10
    count+=1
    if (new==num):
        print(count)
        break