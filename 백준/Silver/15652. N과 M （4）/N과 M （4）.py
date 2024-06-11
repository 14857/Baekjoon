# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = []

def dfs(i):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(i,n+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)