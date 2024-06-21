# 수빈이의 이동 경우의 수 => x-1, x+1,2x
# N(0 ≤ N ≤ 100,000) / K(0 ≤ K ≤ 100,000)
# bfs 이용
# 수빈이가 동생을 찾는 가장 빠른 시간 / 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수

import sys
from collections import deque

n,k = map(int,input().split())

queue = deque()
queue.append(n)

result = 0 # 수빈이가 동생을 찾는 가장 빠른 시간
count = 0
visited = [0]*100001 # 초기 설정


while queue:
    a =  queue.popleft()
    temp = visited[a]
    
    if a == k: # 수빈이가 동생을 찾은 경우
        result = temp # 결과
        count += 1  
        continue
    
    for i in [a-1, a+1, a*2]: # 수빈 이동 경우
        if 0 <= i < 100001 and (visited[i] == 0 or visited[i] == visited[a] +1):
            #범위 안에 있고 방문하지 않았거나, 다음 방문이 이전 방문+1이면
            visited[i] = visited[a] + 1
            queue.append(i)
            
print(result)
print(count)