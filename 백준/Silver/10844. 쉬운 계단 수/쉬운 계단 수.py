# 계단 수 : 인접한 모든 자리의 차이가 1인 수 
# 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램
# N은 1보다 크거나 같고, 100보다 작거나 같은 자연수
# dp 이용

n = int(input())

dp = [[0]*10 for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[n]) % 1000000000)
