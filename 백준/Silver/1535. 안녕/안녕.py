# 세준이의 목표는 주어진 체력내에서 최대한의 기쁨을 느끼는 것
# 세준이의 체력은 100이고, 기쁨은 0
# 세준이의 체력이 0이나 음수가 되면, 죽어서 아무런 기쁨을 못 느낀 것

# 기존 평범한 배낭 문제에서 응
# dp 이용

n = int(input())
L = list(map(int,input().split())) # 잃는 체력
J = list(map(int,input().split())) # 얻는 기쁨

L = [0] + L
J = [0] + J

dp = [[0 for i_ in range(101)] for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,101):
        if L[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])