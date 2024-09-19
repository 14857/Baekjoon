# “1부터 N까지의 수 중에 서로 다른 M개의 수를 골라보세요.
# 저희도 1부터 N까지의 수 중에 서로 다른 M개의 수를 고를건데, 적어도 K개의 수가 같으면 당첨입니다.
# 지민이가 복권에 당첨될 확률을 구하는 프로그램
# combination 원리 이용

from itertools import combinations

n, m, k = map(int,input().split())

ans = 0

all = [*combinations(range(1,n+1), m)]  # 모든 경우의 수

for i in all:
  cnt = 0
  
  for j in range(m):
    if i[j] <= m:  # 0 ~ m-1이 복권 당첨 번호라고 가정
      cnt+=1
  
  if cnt >= k:  # k 개 이상 맞은 경우
    ans += 1

print(ans / len(all)) # 맞는 경우의 수/전체 경우의 수