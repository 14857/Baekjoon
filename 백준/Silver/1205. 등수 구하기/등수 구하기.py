# 등수는 보통 위에서부터 몇 번째 있는 점수인지로 결정한다.
# 같은 점수가 있을 때는 그러한 점수의 등수 중에 가장 작은 등수가 된다.

# 첫째 줄에 N, 태수의 새로운 점수, 그리고 P가 주어진다
# P는 10보다 크거나 같고, 50보다 작거나 같은 정수/ N은 0보다 크거나 같고/ P보다 작거나 같은 정수
# 모든 점수는 2,000,000,000보다 작거나 같은 자연수 또는 0

# 태수의 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하는 프로그램
# 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력

n, score, p = map(int, input().split())

if n == 0:
  print(1)
else:
  rank = list(map(int, input().split()))

  if n == p and rank[-1] >= score:
    print(-1)
  
  else:
    result = n+1
    
    for i in range(n):
      if rank[i] <= score:
        result = i+1
        break
    
    print(result)
