n,m = map(int,input().split())
nlst = list(map(int,input().split()))
mlst = list(map(int,input().split()))

ans = nlst +mlst

ans.sort()
print(*ans)
        