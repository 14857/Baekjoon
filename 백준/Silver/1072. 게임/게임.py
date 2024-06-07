# 이진 탐색 -> start,mid,end 값 정하기
import math
import sys
input=sys.stdin.readline

x,y = map(int,input().split())
z = (100*y)//x

ans = -1
start,end = 1, x

while start <= end:
    mid = (start+end)//2
    
    if ((y+mid)*100//(x+mid)) > z: # end 줄이기
        ans = mid
        end = mid-1
    
    else:
        start = mid+1  

print(ans)
