#  배열이 비어있는데 D를 사용한 경우에는 에러 발생
# 시간 초과 발생. -> 배열 구조 사용하지 않고 deque 이
import sys
from collections import deque

t = int(input())

for _ in range(t):
    p = list(input())# 수행할 함수
    n = int(input()) # 배열에 들어있는 수의 개수
    
    error = 0 #에러 여부
    r = 0
    
    # 입력받은 문자열 arr로 변환
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    
    if n == 0:
        arr = deque()

    # 함수 수행
    for i in p:
        if i == 'R':
            r += 1
            # lst = lst[::-1] -> 마지막에 한번에 계산
            
        elif i == 'D':
            if len(arr) == 0:
                print("error")
                error = 1
                break
            
            else: # R 연산 미룬것 고려하기
                if r % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    
    if error == 0:
        if r % 2 == 0:
            print('[' + ",".join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ",".join(arr) + ']')
