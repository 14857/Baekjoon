# 테스트 케이스의 개수 T(1 ≤ T ≤ 10)
# 동전의 가지 수 N(1 ≤ N ≤ 20)
# N가지 동전으로 만들어야 할 금액 M(1 ≤ M ≤ 10000)
# M를 만드는 경우의 수 -> dp 이용

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    
    n = int(input())
    coins = list(map(int,input().split()))
    m = int(input())

    dp = [0]*(m+1)
    dp[0] = 1

    for i in coins:
        for j in range(i,m+1):
            dp[j] += dp[j-i]

    print(dp[m])