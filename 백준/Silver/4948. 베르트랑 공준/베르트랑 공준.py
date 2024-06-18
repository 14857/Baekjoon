# 이중 for문 이용 + set에서 소수가 아닌 수 제거 -> 시간초과 발생
# 에라토스테네스의 체 이용 & 전체 경우(n범위에 따라) 구하기

num = 123456*2+1
lst = [1]*num

for i in range(1,num):
    if i == 1:
        continue
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                lst[i] = 0
                break

while True:
    n = int(input())
    
    if n == 0:
        break
        
    else:
        ans = 0
        
        for i in range(n+1, 2*n+1):
            ans += lst[i]
            
        print(ans)