n = int(input())

for i in range(1,n+1):
    a = "*" * i + " " * 2*(n-i) + "*" * i
    print(a)

for j in range(1,n):
    b = "*"* (n-j) + " " * 2*j + "*" * (n-j)
    print(b)