x1 = []
y1 = []

for _ in range (3):
    x,y = map(int,input().split())
    x1.append(x)
    y1.append(y)
    

for i in range (3):
    if x1.count(x1[i]) == 1:
        ansx = x1[i]
        break

for i in range (3):
    if y1.count(y1[i]) == 1:
        ansy = y1[i]
        break

print(ansx,ansy)