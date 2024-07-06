#dp 이용

n = int(input())

lst = [0]
lst = lst + (list(map(int,input().split())))

dp = [False]*(n+1)
dp[1] = lst[1]

for i in range(1,n+1):
    for j in range(1,i+1):
        if dp[i] == False:
            dp[i] = lst[j]+dp[i-j]
        else:
            dp[i] = min(dp[i], lst[j]+dp[i-j])

print(dp[n])