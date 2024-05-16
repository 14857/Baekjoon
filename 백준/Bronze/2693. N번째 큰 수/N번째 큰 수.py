t = int(input())
ans = []

for _ in range(t):
    a = list(map(int,input().split()))
    a = sorted(a)
    ans.append(a[-3])

for i in ans:
    print(i)