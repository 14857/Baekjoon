lst = []

n = int(input())

for _ in range(n):
    lst.append(input())

for i in range(n):
    ans = str(i+1) + ". " + lst[i]
    print(ans)