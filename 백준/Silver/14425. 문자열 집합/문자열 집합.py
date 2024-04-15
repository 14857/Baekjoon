n_lst = []
ans = 0

n,m = map(int,input().split())

for i in range(n):
    n_lst.append(input())

for i in range(m):
    s = input()
    
    if s in n_lst:
        ans += 1
        
print(ans)