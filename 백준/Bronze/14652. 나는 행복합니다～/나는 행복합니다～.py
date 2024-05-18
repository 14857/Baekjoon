n,m,k = map(int,input().split())

ans = []

ans.append(k//m)

ans.append(k%m)

print(*ans)