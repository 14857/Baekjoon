t = int(input())

for _ in range(t):
    i,s = map(str,input().split())
    
    i = int(i)
    ans = s[:i-1] + s[i:]
    
    print(ans)