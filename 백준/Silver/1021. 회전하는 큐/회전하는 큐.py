#  N개의 원소를 포함하고 있는 양방향 순환 큐
# 첫 번째 원소 뽑기 / 왼쪽으로 한 칸 이동 / 오른쪽으로 한 칸 이동
# 큐의 크기 N(50보다 작거나 같은 자연수)과 뽑아내려고 하는 수의 개수 M(N보다 작거나 같은 자연수)
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

count = 0

for i in lst:
    while True:
        if dq[0] == i:  # dq의 첫인덱스가 뽑아내려는 수의 위치와 같다면 1번 수행
            dq.popleft()
            break
        
        else: # 위치가 다른 경우
            
            if dq.index(i) < len(dq)/2:  # dq의 길이를 반으로 나눈것보다 작으면 왼쪽으로
                while dq[0] != i: 
                    dq.append(dq.popleft())  
                    count += 1
            
            else:   # dq의 길이를 반으로 나눈것보다 크면 오른쪽으로
                while dq[0] != i:
                    dq.appendleft(dq.pop())  
                    count += 1

print(count)

