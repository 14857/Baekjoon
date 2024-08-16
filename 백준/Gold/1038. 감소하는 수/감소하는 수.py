import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list()               # 모든 감소하는 수

for i in range(1, 11):      #  1~10개의 조합 만들기 : 가장 큰 감수하는 수 9876543210
    for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기(숫자가 중복되는 수는 줄어드는 수 X)
        comb = list(comb)
        comb.sort(reverse=True)                     # 해당 조합 감소하는 수로 변경
        nums.append(int("".join(map(str, comb))))

nums.sort()   # 오름차순 정렬

#print(len(nums)) # 감소하는 수 개수

if n>=len(nums):
    print(-1)
else:
    print(nums[n])

