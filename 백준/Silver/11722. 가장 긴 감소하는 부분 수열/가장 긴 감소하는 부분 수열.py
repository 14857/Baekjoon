n = int(input())

s = list(map(int,input().split()))

reverse_s = s[::-1]
#increase = [1 for i in range(n)]
decrease = [1 for i in range(n)]


for i in range(n):
    for j in range(i):
        if reverse_s[i] > reverse_s[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)
    
print(max(decrease))