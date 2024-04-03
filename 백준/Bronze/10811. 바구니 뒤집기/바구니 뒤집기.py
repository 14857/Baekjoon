# N,M 입력받기
n,m = map(int,input().split())

# N개의 바구니 현황
basket = [i for i in range(1,n+1)]

# M번 동안 공을 넣는 방법 입력받기
for _ in range(m):
    i,j = map(int,input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

# 바구니에 들어있는 공의 번호 출력
print(*basket)