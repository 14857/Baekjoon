# 이진 탐색 -> start,mid,end 값 정하기

import sys
input=sys.stdin.readline

n,m = map(int,input().split())
h = list(map(int,input().split()))
ans = 0

start, end = 1, max(h)

while start <= end:
    mid = (start+end)//2
    sum = 0
    
    for i in h:
        if i > mid:
            sum += i - mid
        
    if sum < m: # 가져갈 수 있는 나무의 합이 부족한 경우 -> 범위 줄이기
        end = mid-1
        
    else: # 가져갈 수 있는 나무의 합이 m이상인 경우
        start = mid+1

print(end)