info = []

n = int(input())

for _ in range(n):
    info.append(list(map(str,input().split())))
    
info = sorted(info, key = lambda x: (int(x[3]), int(x[2]),int(x[1])))

print(info[-1][0])
print(info[0][0])