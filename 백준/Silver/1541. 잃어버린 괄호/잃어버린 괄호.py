n = input().split('-')

for i in range(len(n)):
    if '+' in n[i]:
        n[i] = map(int,n[i].split('+'))
        n[i] = sum(n[i])

ans = int(n[0])

for i in range(1,len(n)):
    ans -= int(n[i])

print(ans)