# 책은 차례대로 박스에 넣는다

n,m = map(int,input().split())
ans = 0

if n == 0:
    print(ans)

else:
    books = list(map(int,input().split()))
    ans = 1
    w = 0
    
    for i in books:
        if w + i <= m:
            w += i
        else:
            ans += 1
            w = i

    print(ans)