#dp 이용

n = int(input())

lst = [0]
lst = lst + (list(map(int,input().split())))

dp = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], lst[j]+dp[i-j])

print(dp[n])