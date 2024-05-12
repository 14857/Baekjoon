# 두 양의 정수 X와 Y가 주어졌을 때,
# Rev(Rev(X) + Rev(Y))를 구하는 프로그램
    
def Rev(x):
    x = str(x)
    new_x = ''
    for i in range(len(x)-1,-1,-1):
        new_x += str(x[i])
    
    return int(new_x)

x,y = map(int,input().split())

ans = Rev(Rev(x)+Rev(y))

print(ans)
