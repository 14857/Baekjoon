# 각 레벨을 클리어할 때 얻는 점수가 주어졌을 때, 몇 번 감소시키면 되는지 구하는 프로그램
# 점수는 항상 양수이어야 하고, 1만큼 감소시키는 것이 1번
# 정답이 여러 가지인 경우에는 점수를 내리는 것을 최소한으로 하는 방법

# 그리디 알고리즘
# 오름차순이 되도록 한다. -> 맨 마지막부터 계산

import sys
input = sys.stdin.readline

score = []
ans = 0

n = int(input())
for _ in range(n):
    score.append(int(input()))
    
for i in range(n-1,0,-1):
    if score[i] <= score[i-1]:
        ans += score[i-1] - score[i] + 1
        score[i-1] = score[i]-1

print(ans)