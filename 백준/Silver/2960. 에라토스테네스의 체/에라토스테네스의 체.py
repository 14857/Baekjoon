N, K = map(int, input().split())

tmp = 0

lst = [True] * (N + 1)

for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if lst[j] != False:
            lst[j] = False
            tmp += 1
            
            if tmp == K:
                print(j)