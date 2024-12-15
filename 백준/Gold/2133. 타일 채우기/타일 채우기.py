# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수
# dp 사용

n = int(input())
dp = [0] * 31
dp[2] = 3

for i in range(4,n+1) :
    if i%2 == 0 :
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else :
        dp[i] = 0

print(dp[n])