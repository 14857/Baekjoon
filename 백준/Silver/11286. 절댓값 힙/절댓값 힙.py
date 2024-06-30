# 절댓값이 가장 작은 값 출력+제거
# 절댓값이 가장 작은 값이 여러 개면 그중 가장 작은 값
# 배열이 비어 있는 경우 + 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
import sys
import heapq
input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    
    x = int(input())
    
    if x != 0:
        heapq.heappush(heap,(abs(x),x))
        
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            