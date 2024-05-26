ans = []

num = int(input())

for i in range(num):
    a,b = map(int,input().split(','))
    ans.append(a+b)
    
for i in ans:
    print(i)