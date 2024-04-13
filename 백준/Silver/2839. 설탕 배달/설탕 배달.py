# 상근이가 배달하는 봉지의 최소 개수를 출력

n = int(input())
ans = 0

while True:
    
    if n == 0:
        break
    
    elif n<3:
        ans = -1
        break
    
    else:
        if n%15 == 0:
            ans += n//15*3
            n = n%15
        
        else:
            if n%5 == 0:
                ans += n//5
                n = n%5
        
            else:
                n = n-3
                ans += 1
                                 
print(ans)   