while True:
    a = list(map(int,input().split()))
    a.sort()
    
    if a == [0,0,0]:
        break
    
    ans = "Scalene"
    
    for i in a:
        
        if a[0] + a[1] <= a[2]:
            ans = "Invalid"
            break
                
        if a.count(i) == 3:
            ans = "Equilateral"
            break
        
        elif a.count(i) == 2:
            ans = "Isosceles"
            break
    print(ans)

