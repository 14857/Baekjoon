# 수열이 들어갈 위치 binary search로 찾기

import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))
lst = [0]

for i in s:
    if lst[-1] < i:
        lst.append(i)
    
    else: # 이분 탐색
        start = 0 #시작지점
        end = len(lst) #종료지점
        
        while start < end:
            mid = (start+end)//2
            
            if lst[mid] < i:
                start = mid + 1
            else:
                end = mid
        lst[end] = i
    
print(len(lst)-1)