n = int(input())
lst = list(map(int,input().split()))
pc = []
cnt = 0

for i in lst:
    if i not in pc:
        pc.append(i)
    else:
        cnt += 1

print(cnt)