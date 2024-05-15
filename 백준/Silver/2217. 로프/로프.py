rope = []
ans = []

n = int(input())

for _ in range(n):
    rope.append(int(input()))

rope.sort()

for i in rope:
    ans.append(i*n)
    n -= 1

print(max(ans))