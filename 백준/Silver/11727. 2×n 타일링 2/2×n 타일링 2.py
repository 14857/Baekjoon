# dp 이용
# 규칙 찾아 점화식 구하기

n = int(input())

dp = [0]*(n+1)
dp[1] = 1

for i in range(2,n+1):
    if i %2 == 1:
        dp[i] = (dp[i-1]*2 -1)%10007
    else:
        dp[i] = (dp[i-1]*2 +1)%10007
        
print(dp[n])