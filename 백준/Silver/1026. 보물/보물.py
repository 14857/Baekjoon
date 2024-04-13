# 첫째 줄에 S의 최솟값을 출력한다.
s = 0
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

for i in range(n):
    s += A[i]*B[i]

print(s)