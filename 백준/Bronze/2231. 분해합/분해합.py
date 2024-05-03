count = 0

n = int(input())

for i in range(n-1,0,-1):
    total = 0
    
    num = i
    total += (i//100000)
    i = (i%100000)
    total += (i//10000) 
    i = (i%10000)
    total += (i//1000)
    i = (i%1000)
    total += (i//100)
    i = (i%100)
    total += (i//10)
    i = (i%10)
    total = total + i + num
    
    
    if total != n:
        count += 0
    else:
        count += 1
        ans = num
        

if count == 0:
    print(0)
else:
    print(ans)