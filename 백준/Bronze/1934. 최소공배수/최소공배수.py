import math
ans = []

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    ans.append(math.lcm(a, b))
    
for i in ans:
    print(i)