import sys

ans = []

n = int(sys.stdin.readline())

for _ in range(n):
    ans.append(int(sys.stdin.readline()))
    
ans.sort(reverse = True)

for i in ans:
    print(i)