# 1,000,000=10**6보다 큰 소수이면 매우 큰 소수

n = int(input())

for _ in range(n):
    ans = "NO"
    
    s = int(input())
    
    for i in range(2,1000001):
        if s%i == 0:
            break
        if i == 1000000:
            ans = "YES"
    
    print(ans)