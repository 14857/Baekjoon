# DP 이용
import sys
input = sys.stdin.readline

n = int(input())
tri = []
dp = [[0]*(n) for _ in range(n)]

for _ in range(n):
    tri.append(list(map(int,input().split())))
    
for i in range(n):
    if i == 0:
        dp[i][0] == tri[0][0]
    
    elif i>=1:
        dp[i][0] = dp[i-1][0] + tri[i][0]
        dp[i][i] = dp[i-1][i-1] + tri[i][i]
    
    for j in range(i+1):
        dp[i][j] = max(tri[i][j] + dp[i-1][j-1], tri[i][j] + dp[i-1][j])

print(max(dp[n-1]))