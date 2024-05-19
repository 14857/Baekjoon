n,m = map(int,input().split())
ans = []
for i in range(n):
    s = input()
    s = s[::-1]
    ans.append(s)

for i in ans:
    print(i)