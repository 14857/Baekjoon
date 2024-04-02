# N,M 입력받기
n,m = map(int,input().split())

# N개의 바구니 현황
basket = [0]*n

# M번 동안 공을 넣는 방법 입력받기
for a in range(m):
    i,j,k = map(int,input().split())
    
    for b in range(i-1,j):
        basket[b] = k

# 바구니에 들어있는 공의 번호 출력
print(*basket)