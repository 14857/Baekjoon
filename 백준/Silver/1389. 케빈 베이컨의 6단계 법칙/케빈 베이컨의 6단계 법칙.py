# 케빈 베이컨의 6단계 법칙
# 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for i in range(n+1)]
ans = []

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    

# bfs 탐색
def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()

        # 친구 관계 확인
        for i in graph[target]:
            
            if not visited[i]:
                visited[i] = visited[target] + 1
                queue.append(i)
                
                
for i in range(1,n+1):
    visited = [0]*(n+1)
    bfs(i)
    ans.append(sum(visited))

print(ans.index(min(ans))+1)
