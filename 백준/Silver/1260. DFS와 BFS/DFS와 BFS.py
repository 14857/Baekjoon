# deque 사용하지 않고도 해결 가능
# 각 함수 내부에 for문 범위는 (1,n+1)으로 수정

def dfs(graph,v,visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v,end = ' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range (1,n+1):
        if visited[i] == False and graph[v][i] == True:
            dfs(graph,i,visited)


def bfs(graph,start,visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = [start]
    # 현재 노드 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        
        v = queue.pop(0)
        print(v,end = ' ')
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들 큐에 삽입
        for i in range (1,n+1):
            if visited[i] == False and graph[v][i] == True:
                queue.append(i)
                visited[i] = True

n,m,v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False]*(n+1)
dfs(graph,v,visited)

print('')

visited = [False]*(n+1)
bfs(graph,v,visited)
