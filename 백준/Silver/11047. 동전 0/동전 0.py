coins = []
ans = 0

n,k = map(int,input().split())


for _ in range (n):
    coins.append(int(input()))

for i in range(n-1,-1,-1):
    
    if k == 0:
       break
    
    
    elif k//coins[i] > 0:
        ans += k//coins[i]
        k = k%coins[i]
        
print(ans)