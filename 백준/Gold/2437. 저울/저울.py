# 무게가 양의 정수인 N개의 저울추가 주어질 때 (N은 1 이상 1,000 이하 / 각 추의 무게는 1이상 1,000,000 이하)
# 이 추들을 사용하여 측정할 수 없는 양의 정수 무게 중 최솟값을 구하는 프로그램

# 그리디 알고리즘, 정렬 
# 수직선 사용하여 풀이를 찾는다.
# 핵심은 측정할 수 있는 무게의 구간을 끊기지 않게 확장시키는 것 -> 누적합 

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 1

for i in arr:
    if ans < i:
        break
    
    ans += i

print(ans)