# 총 N개의 달걀이 있고, 그의 잠재적인 고객은 총 M명
#  각각의 i번째 고객은 각자 달걀 하나를 Pi 가격 이하로 살 수 있다
# A가격에 달걀을 판다고 하면 Pi가 A가격보다 크거나 같은 모든 고객은 달걀을 산다
# 최대 수익을 올릴 수 있는 달걀의 가장 낮은 가격을 책정

n,m = map(int,input().split())
p = []
temp = 0


ans = []

for _ in range(m):
    p.append(int(input()))
    
p.sort()
    
for i in p:
    total = 0
    cnt = 0
    
    
    for j in p:
        if i <= j and cnt < n:
            total += i
            cnt += 1
    
    if total > temp:
        temp = total
        ans = i

print(ans, temp)