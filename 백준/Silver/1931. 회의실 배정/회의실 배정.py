# 끝나는 시간 기준으로 정렬

import sys
input = sys.stdin.readline

n = int(input())
info = []
count = 0
start = 0 # 초기시간

for _ in range(n):
    info.append(list(map(int,input().split())))

info.sort(key = lambda x :(x[1],x[0]))


for a,b in info: # a는 시작 시간, b는 종료 시간
    if start <= a:
        count += 1
        start = b # 이전 타임 종료시간
        
print(count)