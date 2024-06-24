# n가지 종류의 동전 / 그 가치의 합이 k원
# k를 만드는 경우의 수 -> dp 이용
# 순서 생각 X

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []

coins.sort() # 오름차순 정렬

dp = [0]*(k+1)
dp[0] = 1

for _ in range(n):
    coins.append(int(input()))

for i in coins:
    for j in range(i,k+1):
        dp[j] += dp[j-i]

print(dp[k])