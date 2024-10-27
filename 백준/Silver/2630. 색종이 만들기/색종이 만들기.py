# 분할 정복 -> 재귀 이용
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
colored_paper = []

for _ in range(N): 
  colored_paper.append(list(map(int, input().split())))

# 각 종이 개수 
cnt_1 = 0
cnt_0 = 0

# 함수 선언
def slice(x,y,n):
  global cnt_1, cnt_0
  tmp = colored_paper[x][y]
  
  for i in range(x,x+n):
    for j in range(y,y+n):
      if colored_paper[i][j] != tmp:
        slice(x,y,n//2)
        slice(x+n//2,y,n//2)
        slice(x,y+n//2,n//2)
        slice(x+n//2,y+n//2,n//2)
        return
  else:
    if tmp == 0:
      cnt_0 += 1
    else:
      cnt_1 += 1

slice(0,0,N)
print(cnt_0)
print(cnt_1)