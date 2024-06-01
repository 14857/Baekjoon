ans = []

n = int(input())

for _ in range(n):
    count = 0
    n,m = map(int,input().split())
    
    for i in range(n,m+1):
        if str(i).count('0') >= 1:
            count += str(i).count('0')
        
    ans.append(count)

for i in ans:
    print(i)