# sort -> X / dp 이용 -> X
# 우선순위 큐 사용
# 입력이 하나인 경우 고려 -> 조건문으로 구현
import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = []
ans = 0

for _ in range(n):
    heapq.heappush(nums,int(input()))
    
if len(nums) == 0:
    print(ans)
    
else:
    for i in range(n-1):
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        
        ans += a+b
        heapq.heappush(nums,a+b)
    
    print(ans)