n = int(input())
point = []

for _ in range(n):
    point.append(list(map(int,input().split())))
  
ans = sorted(point, key = lambda x : (x[1],x[0]))

for i in range(n):
    print(*ans[i])
