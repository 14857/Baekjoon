# 수빈이의 이동 경우의 수 => x-1, x+1,2x
# N(0 ≤ N ≤ 100,000) / K(0 ≤ K ≤ 100,000)
# bfs 이용
# 곱셈을 최대한 많이 쓸 수 있도록 + 방향의 곱셈과 반대 방향인 뺄셈이 그 다음 우선 순위를 갖는다

import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

queue = deque()
queue.append(n)

result = 0
visited = [-1]*100001 # 초기 설정
visited[n] = 0 


while queue:
    a =  queue.popleft()
    
    if a == k: # 둘이 만났을 때
        print(visited[a]) # 결과
        break
    
    if 0 <= a-1 < 100001 and visited[a-1] == -1:
            visited[a-1] = visited[a] + 1
            queue.append(a-1)
    
    if 0 <= a*2 < 100001 and visited[a*2] == -1:
            visited[a*2] = visited[a]
            queue.appendleft(a*2)
    
    
    if 0 <= a+1 < 100001 and visited[a+1] == -1:
            visited[a+1] = visited[a] + 1
            queue.append(a+1)