# n개의 정수로 이루어진 임의의 수열
# 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합 -> dp 사용
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
ans = [0]*n
ans[0] = lst[0]

for i in range(1,n):
    ans[i] = max(lst[i]+ans[i-1], lst[i])

print(max(ans))