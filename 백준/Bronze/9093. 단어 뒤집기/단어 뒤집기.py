sen = []

t = int(input())

for _ in range(t):
    sen.append(list(map(str,input().split())))

for i in range(t):
    
    for j in range(len(sen[i])):
        sen[i][j] = sen[i][j][::-1]
    
    ans = " ".join(sen[i])
    print(ans)