colors = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

ans = ''

for _ in range(2):
    
    a = input()
    
    for i in range(10):
        if colors[i] == a:
            ans += str(i)
            continue

b = input()
    
for i in range(10):
    if colors[i] == b:
        ans = int(ans)*(10**i)

print(ans)