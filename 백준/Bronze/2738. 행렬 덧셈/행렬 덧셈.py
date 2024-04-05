N,M = map(int,input().split())
A = []
B = []

for _ in range(N):
    n = list(map(int,input().split()))
    A.append(n)
    
for _ in range(N):
    n = list(map(int,input().split()))
    B.append(n)

for i in range(N):
    for a in range(M):
        print(A[i][a] + B[i][a], end = ' ')
    print()
