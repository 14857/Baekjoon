n = list(map(int,input().split()))
sorted_n = sorted(n)

while True:
    if n == sorted_n:
        break
    else:
        for i in range(len(n)-1):
            if n[i] > n[i+1]:
                n[i],n[i+1] = n[i+1],n[i]
                print(*n)
                