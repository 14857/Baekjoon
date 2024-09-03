#  N개의 빨대 중에 3개의 빨대를 선택 -> 삼각형 만들
# 세 변의 길이의 합의 최댓값
# 중첩 for문 -> 시간초과 발생 => for 문 줄이기
import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse = True)

for i in range(n-2):
    if nums[i] < nums[i+1] + nums[i+2]:
                print(nums[i] + nums[i+1] + nums[i+2])
                exit()
                
print(-1)
