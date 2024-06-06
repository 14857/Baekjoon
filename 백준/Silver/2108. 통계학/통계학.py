import sys
input = sys.stdin.readline

nums = []
nums_count = {}
nums_sum = 0
ans3 = []

n = int(input())

for _ in range(n):
    
    a = int(input())
    nums.append(a)
    
    nums_sum += a
    
    if a in nums_count:
        nums_count[a] += 1
    else:
        nums_count[a] = 1

nums = sorted(nums)

# 최빈값 계산 - ans
count = 0
for i in nums_count:
    if nums_count[i] == max(nums_count.values()):
        ans3.append(i)

ans3 = sorted(ans3)

if len(ans3) == 1:
    ans = ans3[0]
else:
    ans = ans3[1]


# output
print(round(nums_sum/n)) # 산술 평균
print(nums[n//2]) # 중앙값
print(ans) # 최빈값
print(nums[-1]-nums[0]) # 범위