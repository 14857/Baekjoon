import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

nums = list()

for i in range(1, 11):      # 자릿수가 1~10개의 조합
    for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)                # 해당 조합 감소하는 수로 경
        nums.append(int("".join(map(str, comb))))

nums.sort()   # 오름차순

try:
    print(nums[n - 1])
except:     # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
    print(-1)
