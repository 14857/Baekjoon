# 정렬하여 1차의 1등을 기준으로 잡았을 때, 합격하기 위해서는 1등의 2차 등수보다 높아야 한다.
#  테스트 케이스의 개수 T(1 ≤ T ≤ 20) /  지원자의 숫자 N(1 ≤ N ≤ 100,000)
# 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수

import sys
input = sys.stdin.readline
        
T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    arr.sort()

    cnt = 1
    max_ = arr[0][1]
    
    for i in range(1,N):
        if max_ > arr[i][1]:
            cnt += 1
            max_ = arr[i][1]
            
    print(cnt)
