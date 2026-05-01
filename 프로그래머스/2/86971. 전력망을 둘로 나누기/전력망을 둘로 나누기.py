# 완전탐색 > 전력망을 둘로 나누기
# 각 전선을 하나씩 제거 → 두 덩어리의 노드 개수 차이를 계산 → 최소값 찾기

from collections import deque

def solution(n, wires):
    answer = n  # 최대 차이로 초기화
    
    for i in range(len(wires)):
        # i번째 전선 제거
        graph = [[] for _ in range(n+1)]
        
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)
        
        # BFS로 한 쪽 그룹 크기 계산
        visited = [False] * (n+1)
        queue = deque([1])
        visited[1] = True
        count = 1
        
        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1
        
        # 두 그룹 차이 계산
        diff = abs(n - 2 * count)
        answer = min(answer, diff)
    
    return answer