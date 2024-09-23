#  앞에 있는 상자의 크기 < 뒤에 있는 상자의 크기 -> 앞에 있는 상자를 뒤에 있는 상자 안에 넣을 수 있다

n = int(input())
lst = list(map(int,input().split()))
 
dp = [1]*(n)
 
for i in range(1,n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))
