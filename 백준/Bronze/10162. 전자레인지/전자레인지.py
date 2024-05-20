a = 300
b = 60
c = 10

ans = [0,0,0]

t = int(input())

if t%10 != 0:
    print(-1)
else:
    ans[0] = t//a
    t = t%a
    
    ans[1] = t//b
    t = t%b
    
    ans[2] = t//c

    print(*ans)