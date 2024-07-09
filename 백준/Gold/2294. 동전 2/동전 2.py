# dp
# n가지 종류의 동전, 가치의 합이 k
# 동전의 개수가 최소가 되도록 한다
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

coins = []
dp = [100001]*(k+1)
dp[0] = 0

for _ in range(n):
    coins.append(int(input()))

for num in coins:
    for i in range(num, k+1):
       dp[i] = min(dp[i],dp[i-num]+1)
    
if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])