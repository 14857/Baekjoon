lst = list(map(int,input().split()))

total = 0

for i in range(len(lst)):
    total += lst[i]*lst[i]
    
print(total%10)
