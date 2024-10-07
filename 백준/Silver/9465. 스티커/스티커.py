# dp[i][j] : 해당 스티커를 마지막으로 골랐을 때의 최대 가치

t = int(input())

for _ in range(t):
    
    stickers = []
    
    n = int(input())
    
    dp = [[0]*n,[0]*n]
    
    for _ in range(2):
        stickers.append(list(map(int,input().split())))
    
    # n이 1인 경우
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    
    if n == 1:
        print(max(dp[0][0],dp[1][0]))
        continue
    
    dp[0][1] = stickers[1][0] + stickers[0][1]
    dp[1][1] = stickers[0][0] + stickers[1][1]
    
    if n == 2:
        print(max(dp[0][1],dp[1][1]))
        continue
    
    for i in range(2,n):
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + stickers[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + stickers[1][i]
        
    
    print(max(dp[0][-1], dp[1][-1]))