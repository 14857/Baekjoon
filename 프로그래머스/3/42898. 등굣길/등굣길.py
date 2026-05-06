# 동적계획법(Dynamic Programming) > 등굣길 -> 2차원 배열 사용
# 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지 반환

import math

def solution(m, n, puddles):
    answer = 0
    num = 1000000007
    
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            
            if [j,i] in puddles:
                dp[i][j] = 0
                continue
            
            if i == 1 and j == 1:
                continue
            
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % num
    
    answer =  dp[n][m]
    return answer