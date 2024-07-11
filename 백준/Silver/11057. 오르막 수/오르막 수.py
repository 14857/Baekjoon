# 오르막 수의 개수를 구하는 프로그램
# N (1 ≤ N ≤ 1,000)
# dp

n = int(input())
nums = [[] for _ in range (n+1)]
nums[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1):
    for j in range(0,10):
        nums[i].append(sum(nums[i-1][j:]))


print(sum(nums[n])%10007)