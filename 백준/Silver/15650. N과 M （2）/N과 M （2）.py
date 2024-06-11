# 수열은 사전 순으로 증가하는 순서로 출력

n,m = map(int,input().split())
s = []

def dfs():
    if len(s) == m:
        if s == sorted(s):
            print(' '.join(map(str,s)))
            return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()