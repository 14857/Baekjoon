# del 이용 -> 시간초과 발생
# 해결 방법 : deque와 queue 이용 -> deque의 popleft() 메소드를 사용

import sys
from collections import deque

n = int(input())
n_lst = deque([i for i in range(1,n+1)])

while True:
    if len(n_lst)==1:
        print(*n_lst)
        break

    else:
        n_lst.popleft() # 최상단의 카드 버리기
        card = n_lst.popleft() # 카드 버린 후 제일 위에 있는 카드
        n_lst.append(card) # 제일 아래로 이동

