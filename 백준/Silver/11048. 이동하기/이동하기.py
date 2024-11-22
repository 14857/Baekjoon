# 미로의 가장 왼쪽 윗 방은 (1, 1)이고, 가장 오른쪽 아랫 방은 (N, M)
# N개 줄에는 총 M개의 숫자가 주어지며, r번째 줄의 c번째 수는 (r, c)에 놓여져 있는 사탕의 개수다
# 준규가 (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있다 -> 오른쪽, 아래, 오른쪽 대각선 아래
# 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하는 프로그램

# dp 이용

n,m = map(int,input().split())
maze = []
dp = [[0]*(m+1) for _ in range(n+1)]

for _ in range (n):
    maze.append(list(map(int,input().split())))
    
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = maze[i-1][j-1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
print(dp[n][m])