# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램
from itertools import combinations, permutations

n = int(input())

nums = [i for i in range(1,n+1)]

ans = list(permutations(nums,n))

for i in ans:
    print(*i)