#최솟값을 위해서는 모든 - 뒤에 괄호 생성 → - 뒤에 있는 값이 최대가 됨
#0으로 시작하는 숫자는 eval에서 오류 → 다른 방법 사용

a = list(input().split('-'))
ans = sum(list(map(int, a[0].split('+'))))

for i in range(1, len(a)):
    ans-=sum(list(map(int, a[i].split('+'))))

print(ans)