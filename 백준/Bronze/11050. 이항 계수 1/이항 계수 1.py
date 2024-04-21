n,k = map(int,input().split())
a = 1
b = 1

#분자 계산
for _ in range(k):
    a *= n
    n = n-1

#분모 계산
for i in range(k,0,-1):
    b *= i

print(a//b)
    