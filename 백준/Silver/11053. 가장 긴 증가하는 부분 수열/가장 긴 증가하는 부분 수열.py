# dp 이용

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

count = [1]*n

for i in range(1,n):
    for j in range(i): # j의 인덱스가 i보다 더 작음
        if lst[i] > lst[j]:
            count[i] = max(count[i], count[j]+1)

print(max(count))