# 이미 심어져 있는 가로수의 수를 나타내는 하나의 정수 N
# 둘째 줄부터 N개의 줄 ->  각 줄마다 심어져 있는 가로수의 위치
import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
a = int(input())

location = []

for i in range(N-1):
    num = int(input())
    location.append(num - a)
    a = num

g = location[0]
for j in range(1, len(location)):
    g = gcd(g, location[j])

result = 0
for each in location:
    result += each // g - 1
    
print(result)