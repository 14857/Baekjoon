a = set()
both = []

n,m = map(int,input().split())

for _ in range(n):
    a.add(input())

for _ in range(m):
    
    b = input()
    if b in a:
        both.append(b)

both.sort()

print(len(both))

for i in both:
    print(i)