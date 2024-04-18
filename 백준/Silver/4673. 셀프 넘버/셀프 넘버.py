lst = [0]*10001

for i in range(10001):
    if i>=10:
        total = i
        s = list(str(i))
        for a in range (len(s)):
            total += int(s[a])
        
        if total<10001:
            lst[total] = 1
    
    else:
        lst[i+i] = 1


for i in range(10001):
    if lst[i] == 0:
        print(i)