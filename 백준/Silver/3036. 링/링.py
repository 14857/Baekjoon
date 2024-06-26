from math import gcd
import sys

n = int(input())

nums = list(map(int,input().split()))

for i in range(1, n):
    t = gcd(nums[0], nums[i])
    print(f'{nums[0] // t}/{nums[i] // t}')