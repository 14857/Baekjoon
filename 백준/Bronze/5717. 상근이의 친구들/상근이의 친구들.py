ans = []
while True:
    m,f = map(int,input().split())
    if m ==0 and f == 0:
        break
    
    else:
        ans.append(m+f)
        
for i in ans:
    print(i)