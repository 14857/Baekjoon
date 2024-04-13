n = int(input())
p = list(map(int,input().split()))
p.sort()

time = []
total = 0
for i in range(n):
    total += p[i]
    time.append(total)

print(sum(time))