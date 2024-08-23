# 한 개 이상의 서로 다른 3의 제곱수의 합으로 표현되는 N번째로 작은 수
# dp 그래프 작성 X
# 증가량이 2의 배수임을 이용한다.

n = bin(int(input()))[2:]
ans = 0

for i in range(len(n)):
    if int(n[i]) == 1:
        ans += 3**(len(n)-i-1)
print(ans)