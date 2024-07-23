import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = []

for _ in range(n):
    s,t = map(int,input().split())
    time.append([s,t])

time.sort(key = lambda x : (x[0],x[1]))

heap = [time[0][1]]

for i in range(1,n):
    if heap[0] <= time[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,time[i][1])

print(len(heap))
    