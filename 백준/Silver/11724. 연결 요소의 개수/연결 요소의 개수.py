import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(graph,v,visited):
    # 현재 노드 방문 처리
    visited[v] = True
    # print(v,end = ' ') # 처리 순서
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range (1,n+1):
        if visited[i] == False and graph[v][i] == True:
            dfs(graph,i,visited)

n,m = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

count = 0

visited = [False]*(n+1)

for i in range(1,n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        count += 1

print(count)

