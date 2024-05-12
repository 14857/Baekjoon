files = []
ans = ''

n = int(input())

for _ in range(n):
    files.append(input())
    
for j in range(len(files[0])):
    correct = 1
    
    for i in range(1,n):
        if files[0][j] != files[i][j]:
            correct = 0
    
    if correct == 1:
        ans += files[0][j]
    else:
        ans += '?'

print(ans)