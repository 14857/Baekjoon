ans = []

while True:
    name,age,weight = map(str,input().split())
    
    if name == '#' and age == '0' and weight == '0':
        break
    
    else:
        if int(age) > 17 or int(weight) >= 80:
            ans.append([name,"Senior"])
        
        else:
            ans.append([name,"Junior"])
            
for i in ans:
    print(*i)