# 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
# 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)
# dp

import sys
input = sys.stdin.readline
nums = []

n,k = map(int,input().split())
dp = [0 for _ in range(k+1)]

for _ in range(n):
    w,v = map(int,input().split())
    nums.append([w,v])
    
for i in nums:
    w = i[0]
    v = i[1]
    
    for j in range(k,w-1,-1):
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[-1])
