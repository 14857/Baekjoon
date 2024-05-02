t = int(input())

for _ in range(t):
    h,w,n = map(int,input().split())
    floor = n%h  
    room = n//h+1
    
    if floor == 0:
        floor = h
        room -= 1
    
    if room < 10:
        ans =str(floor) + '0' + str(room)
    else:
        ans = str(floor) + str(room)
    

    print(ans)