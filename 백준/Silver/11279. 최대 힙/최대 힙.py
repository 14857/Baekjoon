# list + append 사용 -> 시간초과 발생
# heapq 사용 -> 최소힙에서 부호 바꿔 최대힙 구현
import sys
import heapq
input = sys.stdin.readline

q = []
n = int(input())

for _ in range(n):    
    x = int(input())
    
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(-heapq.heappop(q))   
    else:
        heapq.heappush(q,-x)