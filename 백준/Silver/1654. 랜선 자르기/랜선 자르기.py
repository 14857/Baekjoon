# 이진 탐색 -> start,mid,end 값 정하기
# 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
#  N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력

import sys
input=sys.stdin.readline

k,n = map(int,input().split())
h = []

for _ in range(k):
    h.append(int(input()))

start, end = 1, max(h)

while start <= end:
    mid = (start+end)//2
    sum = 0
    
    for i in h:
        if i >= mid:
            sum += i//mid
        
    if sum < n: 
        end = mid-1
        
    else:
        start = mid+1

print(end)