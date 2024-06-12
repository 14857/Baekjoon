t = int(input())

num = [0]*101

num[1] = 1
num[2] = 1
num[3] = 1

for i in range(3,101):
    num[i] = num[i-2] + num[i-3]
    
for _ in range(t):
    n = int(input())
    print(num[n])