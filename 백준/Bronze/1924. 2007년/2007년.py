month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
x,y = map(int,input().split())
days = y

# 28일 2월
for i in range(x):
    days += month[i]

if days%7 == 1:
    ans = 'MON'
    
elif days%7 == 2:
    ans = 'TUE'
     
elif days%7 == 3:
    ans = 'WED'
        
        
elif days%7 == 4:
    ans = 'THU'
        
        
elif days%7 == 5:
    ans = 'FRI'
        
elif days%7 == 6:
    ans = 'SAT'
        
else:
    ans = 'SUN'

print(ans)