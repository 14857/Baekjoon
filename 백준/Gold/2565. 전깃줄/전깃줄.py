# 전깃줄의 개수(n)는 100 이하의 자연수
# 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때
# 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램
# A의 번호가 작은 순서대로 정렬 + 앞순서의 B가 뒷순서의 B보다 작은 경우가 최대
# dp 이용

n = int(input())

info = []
dp = [1]*n

for _ in range(n):
    info.append(list(map(int,input().split())))
    
info.sort()

for i in range(1, n):
  for j in range(0, i):
    if info[j][1] < info[i][1]:
      dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))