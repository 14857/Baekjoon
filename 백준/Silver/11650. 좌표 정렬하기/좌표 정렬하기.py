n = int(input())
dots = []

for _ in range(n):
    dot = list(map(int,input().split()))
    dots.append(dot)
        
dots.sort()

for i in range(n):
    print(*dots[i])