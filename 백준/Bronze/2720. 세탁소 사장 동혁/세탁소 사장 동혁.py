ans = []

t = int(input())

for _ in range(t):
    c = int(input())
    
    q = c//25
    c = c%25
    
    d = c//10
    c = c%10
    
    n = c//5
    c = c%5
    
    ans.append([q,d,n,c])

for i in ans:
    print(*i)
