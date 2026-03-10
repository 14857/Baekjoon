import sys

n = int(sys.stdin.readline())

xs = []
ys = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xs.append(x)
    ys.append(y)

width = max(xs) - min(xs)
height = max(ys) - min(ys)

print(width * height)