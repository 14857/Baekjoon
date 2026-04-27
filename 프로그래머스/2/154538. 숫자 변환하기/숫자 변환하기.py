# 연습문제 > 숫자 변환하기
# Greedy X -> BFS
from collections import deque

def solution(x, y, n):
    answer = 0
    
    queue = deque([(x, 0)])  # (현재 값, 연산 횟수)
    visited = set([x])
    
    while queue:
        cur, cnt = queue.popleft()
        
        if cur == y:
            return cnt
        
        for next in (cur + n, cur * 2, cur * 3):
            if next <= y and next not in visited:
                visited.add(next)
                queue.append((next, cnt + 1))
    
    return -1