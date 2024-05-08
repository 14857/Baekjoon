s = int(input())

for i in range(1,s+1):
    total = i*(i+1)/2
    
    if s - total <= i:
        print(i)
        break
        
