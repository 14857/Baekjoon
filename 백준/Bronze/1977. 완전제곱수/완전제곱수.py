ans = []

m = int(input())
n = int(input())

for i in range(m,n+1):
    for j in range(1,i+1):
        if i/j==j:
            ans.append(i)

if len(ans) == 0:
    print(-1)

else:
    print(sum(ans))
    print(min(ans))