# 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)
# C개의 공유기를 N개의 집에 적당히 설치해서
# 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
# 정렬, 이분탐색 (투 포인터 사용)

import sys
input = sys.stdin.readline

n,c = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

# 초기값 설정 -> 앞 집부터 공유기 설치
start = 1
end = arr[-1] - arr[0]
ans = 0

while (start <= end):
    mid = (start + end) // 2 # 설치 거리
    current = arr[0]
    count = 1
    
    for i in range(1,len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]
    
    if count >= c: # 더 넓게 설치할 수 있다는 의미 -> 설치 거리를 늘린
        start = mid+1
        ans = mid
    
    else: # 더 좁게 설치해야 한다는 의미 -> 설치 거리를 줄인다
        end = mid-1
    

print(ans)