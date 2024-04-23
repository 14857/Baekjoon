# 끊어진 기타줄의 개수 N / 기타줄 브랜드 M
# 기타줄 6개가 들어있는 패키지의 가격 / 낱개로 살 때의 가격
# 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램

# 가장 효율적인 브랜드 선택 후 돈의 수 계산

n,m = map(int,input().split())
pack1 = []
one1 = []
ans = 0

for _ in range(m):
    pack,one = map(int,input().split())
    
    pack1.append(pack)
    one1.append(one)

# 가장 효율적인 선택
pack = min(pack1)
one = min(one1)

# 최소 돈 계산

while True:
    if n == 0:
        break
    
    else:
        if n<=6:
            if (n*one)<pack:
                ans += n*one
                n = 0
            else:
                ans += pack
                n = 0
        
        else: #6개보다 많이 사는 경우
            if (one*6 > pack): #pack이 더 싸다면
                ans += n//6*pack
                n = n%6
            else:
                ans += n*one
                n=0
                
print(ans)