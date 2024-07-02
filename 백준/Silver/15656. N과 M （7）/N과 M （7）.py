n,m = map(int,input().split())
lst = list(map(int,input().split()))
s = []

lst.sort()

def dfs():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(n):
        s.append(lst[i])
        dfs()
        s.pop()
        
dfs()
