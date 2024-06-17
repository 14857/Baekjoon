import sys
input = sys.stdin.readline

point = []
direction = []

max1 = 0
max2 = 0

k = int(input())

for _ in range(6):
    a,b = map(int,input().split())
    
    point.append([a,b])
    direction.append(a)

for i in range(6): # 전체 직사각형 면적
    if point[i][0] == 1 or point[i][0] == 2:
        if point[i][1] > max1:
            max1 = point[i][1]
            
    elif point[i][0] == 3 or point[i][0] == 4:
        if point[i][1] > max2:
            max2 = point[i][1]
total1 = (max1*max2)            
        
# 빼야하는 면적
if direction == [1,3,1,4,2,3] or direction ==[4,1,4,2,3,1] or direction ==[2,4,2,3,1,4] or direction ==[3,2,3,1,4,2]:
    total2 = point[0][1]*point[1][1]
    
elif direction == [3,1,4,2,3,1] or direction ==[1,4,2,3,1,4] or direction ==[4,2,3,1,4,2] or direction ==[2,3,1,4,2,3]:
    total2 = point[0][1]*point[-1][1]

else:
    for i in range(0,4): 
        
        if point[i][0] == point[i+2][0]:
            total2 = point[i+1][1]*point[i+2][1]
            break
        
print((total1-total2)*k)
