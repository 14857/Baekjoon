ans = 0

n = int(input())
nlst = list(map(int,input().split()))

for i in range (n):
    count = 0 # 소수 판별용
    
    if nlst[i] != 1:
        for k in range(2,nlst[i]):
            if nlst[i]%k == 0:
                count += 1
    
    else: #1은 예외
        count += 1
    
    if count == 0:
        ans += 1

print(ans)