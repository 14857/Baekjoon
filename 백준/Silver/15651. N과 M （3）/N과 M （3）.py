# 수열은 사전 순으로 증가하는 순서로 출력
# 같은 수 여러 번 선택 가능

n,m = map(int,input().split())
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        s.append(i)
        dfs()
        s.pop()
dfs()