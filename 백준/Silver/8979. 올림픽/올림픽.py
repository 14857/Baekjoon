n,k = map(int,input().split())

lst = []

for _ in range(n):
    lst.append(list(map(int,input().split())))

lst.sort(key = lambda x : (x[1],x[2],x[3]), reverse = True)

idx = [lst[i][0] for i in range(n)].index(k)

for i in range(n):
    if lst[idx][1:] == lst[i][1:]:
        print(i+1)
        break