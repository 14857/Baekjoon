n = int(input())
x,y = map(int,input().split())
m = int(input())
result = []
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 이용
def dfs(v, num):
    # 현재 노드 방문 처리
    visited[v] = True
    num += 1

    if v == y:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i,num)

dfs(x,0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)