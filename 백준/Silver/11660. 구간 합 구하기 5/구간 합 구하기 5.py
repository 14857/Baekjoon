# ans += lst[i][j] -> 시간 초과 발생 -> dp 이용하기

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lst = []
dp = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    lst.append(list(map(int,input().split())))
    

for i in range(1, n + 1): # 합에 대한 dp
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + lst[i-1][j-1]


for _ in range(m):
    
    x1, y1, x2, y2 = map(int,input().split())
    
    ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1] # 전체에서 뺀 후 겹치는 부분 계산
    
    print(ans)