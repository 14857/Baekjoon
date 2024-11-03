# 백트래킹 이용
# N개의 자연수와 자연수 M이 주어졌을 때, 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 고른 수열은 비내림차순이어야 한다
# 수열은 사전 순으로 증가하는 순서로 출력 -> sort 이용

import sys
input = sys.stdin.readline

def back_tracking(idx, temp):  
    if len(temp) == m:  
        if not tuple(temp) in result:  
            print(*temp)  
            result.add(tuple(temp))  
    for i in range(idx, n):  
        temp.append(nums[i])  
        back_tracking(i+1, temp)  
        temp.pop() 



n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans = []

nums.sort()

result = set()  
back_tracking(0, ans)
