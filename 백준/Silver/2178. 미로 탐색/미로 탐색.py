# BFS 이용 -> 최단 거리, 최단 횟수를 구하는 경우
from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int,input().split())

# 2차원 리스트 생성하기
graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]
queue = deque([(0,0)])

# 미로 이동 표현하기
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0

while queue:
    x,y = queue.popleft()
    for i in range(4):
        next_x,next_y = x+dx[i], y+dy[i]
        
        if 0<= next_x < N and 0<= next_y<M:
            if graph[next_x][next_y] == 1:
                queue.append((next_x,next_y))
                graph[next_x][next_y] = graph[x][y]+1

print(graph[N-1][M-1])
        
