a,b = map(int,input().split())

nums = []

for i in range(1,b+1):
    for j in range(i):
        nums.append(i)

ans = sum(nums[a-1:b])

print(ans)