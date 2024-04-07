# 첫째 줄부터 다섯 번째 줄까지 한 줄에 하나씩 자연수가 주어진다
# 첫째 줄에는 평균 출력 / 둘째 줄에는 중앙값 출력
# 평균과 중앙값은 모두 자연수이다.

nums = []

for i in range(5):
    nums.append(int(input()))

nums.sort()

print(sum(nums)//5)
print(nums[2])