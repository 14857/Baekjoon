while True:
    a,b,c = map(int,input().split())
    
    if a ==0 and b==0 and c==0:
        break
    
    else:
        if max(a,b,c) == a:
            if a*a == b*b +c*c:
                print("right")
            else:
                print("wrong")
                
        
        elif max(a,b,c) == b:
            if b*b == a*a +c*c:
                print("right")
            
            else:
                print("wrong")
        
        elif max(a,b,c) == c:
            if a*a + b*b  == c*c:
                print("right")
            
            else:
                print("wrong")

