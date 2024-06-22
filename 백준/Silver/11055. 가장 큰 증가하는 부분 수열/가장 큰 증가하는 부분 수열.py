n = int(input())

s = list(map(int,input().split()))

#reverse_s = s[::-1]
increase = [a for a in s]

for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            increase[i] = max(increase[i], increase[j]+s[i])
        
print(max(increase))