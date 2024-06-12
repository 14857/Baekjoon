# 계단은 한 번에 하나 혹은 두 개씩
# 연속된 세 개의 계단을 모두 밟아서는 X
# 마지막 계단은 무조건 도착
# DP 사용
n = int(input())

point = [0]
ans = [0]*(n+1)

for _ in range(n):
    point.append(int(input()))

if n == 1:
    result = sum(point)
    
elif n == 2:
    result = sum(point)

else:
    ans[1] = point[1]
    ans[2] = point[1] + point[2]
    
    for i in range(3,n+1):
        ans[i] = max(ans[i-2]+point[i], ans[i-3]+point[i]+point[i-1])
    result = ans[-1]

print(result)
