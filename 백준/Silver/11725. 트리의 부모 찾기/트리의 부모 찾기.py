# 2차원 리스트 저장 -> 메모리 초과
# 메모리 탐색 -> dfs 사용
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1)

for i in range(2, n+1):
    print(visited[i])
