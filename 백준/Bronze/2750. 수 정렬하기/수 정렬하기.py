# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과 -> 한 줄에 하나씩 출력
n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

nums.sort()

for i in range(n):
    print(nums[i])