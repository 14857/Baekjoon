ans = []

x,y,w,h = map(int,input().split())

ans.append(x)
ans.append(y)
ans.append(w-x)
ans.append(h-y)

print(min(ans))
