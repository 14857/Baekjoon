a = int(input())
b = int(input())
ans = []

for i in range(a,b+1):
    
    count = 0
    
    for j in range(2,i):
        if i%j ==0:
            count = 1
    
    if count == 0 and i != 1:
        ans.append(i)

if len(ans) == 0:
    print(-1)

else:
    print(sum(ans))
    print(min(ans))