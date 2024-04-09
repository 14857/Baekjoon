# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램

import sys
input = sys.stdin.readline

n = int(input())
ans = []

for i in range (n):
    ans.append(int(input()))

ans.sort()

for i in range(len(ans)):
    print(ans[i])