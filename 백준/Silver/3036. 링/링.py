# 링의 반지름이 주어진다. 이때, 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램
# 링의 개수 N, 링의 반지름
# 기약 분수 형태 A/B로 출력 -> gcd 사용

from math import gcd
import sys

n = int(input())

nums = list(map(int,input().split()))

for i in range(1, n):
    t = gcd(nums[0], nums[i])
    print(f'{nums[0] // t}/{nums[i] // t}')