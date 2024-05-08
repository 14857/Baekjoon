t = int(input())

for _ in range(t):
    k = int(input()) #층수
    m = int(input()) #호수
    
    a = [x for x in range(1,m+1)] #0층 각 호수
    
    for j in range(k):
        for i in range(1,m):
            a[i] += a[i-1]
    
    print(a[-1])
        
        