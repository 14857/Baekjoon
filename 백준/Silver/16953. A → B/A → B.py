#bfs 이용하여 풀기 -> 모든 경우 큐에 넣기
from collections import deque

a,b = map(int,input().split())

def solve(a, b):
    q = deque([(a, 1)])

    while q:
        now, cnt = q.popleft()
        if now == b:
            print(cnt)
            return

        if now * 2 <= b:
            q.append((now * 2, cnt + 1))
        if now * 10 + 1 <= b:
            q.append((now * 10 + 1, cnt + 1))
    print(-1)


solve(a, b)