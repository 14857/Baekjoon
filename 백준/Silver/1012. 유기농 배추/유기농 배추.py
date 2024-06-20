# RecursionError 발생 -> 해결
import sys
sys.setrecursionlimit(10000)

# 배추밭의 가로길이 M(1 ≤ M ≤ 50) / 세로길이 N(1 ≤ N ≤ 50)
# 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
# K줄에는 배추의 위치 X(0 ≤ X ≤ M-1) / Y(0 ≤ Y ≤ N-1)
# 각 테스트 케이스에 대해 필요한 최소 배추흰지렁이 마리 수 출력

def dfs(x,y):
    
    global count
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n): # graph 범위 안에 들어있는지 확인
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0 # 확인 처리
                dfs(nx, ny)
           
t = int(input()) # 테스트 케이스 횟수

for _ in range(t):

    total = 0    
    
    m,n,k = map(int,input().split())
    
    graph = [[0]*(m) for _ in range(n)]

    for i in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1

    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i,j)
                total += 1
                
    print(total)