# 사자들을 우리에 가둘 때, 가로로도 세로로도 붙어 있게 배치 불가
# 2*N 배열에 사자를 배치하는 경우의 수
# 사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수로 친다고 가정
# 사자를 배치하는 경우의 수를 9901로 나눈 나머지

import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(3)

else: 
    dp = [1]*(n+1)
    dp[1] = 3
    dp[2] = 7

    for i in range(3,n+1) :
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
        
    print(dp[n])