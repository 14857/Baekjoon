n,m = map(int,input().split())
lst = list(map(int,input().split()))
s = []

lst.sort()

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(start,n):
        s.append(lst[i])
        dfs(i+1)
        s.pop()
        
dfs(0)
