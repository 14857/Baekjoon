ans = []
while True:
    a = input()
    sen = ''
    if a == 'END':
        break
    
    else:
        for i in range(len(a)-1,-1,-1):
            sen += a[i]
        ans.append(sen)
        
for i in ans:
    print(i)