
# 1 ≤ N, M ≤ 9

def correct(a): # 제곱수 판별
    a = int(a)
    
    if int(a**0.5)**2 == a:
        return True
    else:
        return False

n,m = map(int,input().split())

lst = []
ans = -1

for _ in range(n):
    lst.append(list(input()))
    
for i in range(n):
    for j in range(m):
        for rowd in range(-n,n): # 행의 등차
            for cold in range(-m,m): # 열의 등차
                
                s = ''
                x,y = i,j
                
                if rowd == 0 and cold == 0:
                    continue
                
                while 0<= x < n and 0<= y < m:
                    s += lst[x][y]                 
                    if correct(s):# 제곱수 판
                        ans = max(ans,int(s))
                    
                    x += rowd
                    y += cold

print(ans)