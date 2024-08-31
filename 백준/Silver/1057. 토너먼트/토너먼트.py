# 인접한 번호끼리 스타 ->  이긴 사람은 다음 라운드에 진출하고, 진 사람은 그 라운드에서 떨어진다
# 라운드의 참가자가 홀수명이라면, 마지막 번호를 가진 참가자는 다음 라운드로 자동 진출
import math

n,k,l = map(int,input().split())

ans = 0

while True:
    if k == l:
        print(ans)
        break
    
    k = math.ceil(k/2)
    l = math.ceil(l/2)
    ans += 1