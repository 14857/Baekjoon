import math

a = 0
nums = [0]*10

n = input()

for i in range(len(n)):
    nums[int(n[i])] += 1


for i in (0,1,2,3,4,5,7,8): #6,9를 제외하고 가장 큰 값
    if nums[i] > a:
        a = nums[i]

b = math.ceil((nums[6]+nums[9])/2)

print(max(a,b))