n = int(input())

point = []

for _ in range(n):
    point.append(list(map(int,input().split())))

for  i in range(n):
    if point[i][0] == point[i][3] and point[i][1] == point[i][4]:
        if point[i][2] == point[i][5]: # 위치가 무한대인 경우
            result = -1
        else: # r1,r2 값이 다른 경우 -> 교차점 존재 X
            result = 0
    else:
        d = ((point[i][0]-point[i][3])**2 + (point[i][1]-point[i][4])**2)**0.5
        r_s = point[i][2] + point[i][5] # 반지름의 합
        r_m = abs(point[i][2] - point[i][5]) # 반지름의 차
        
        if r_m < d and d < r_s:
            result = 2
        elif r_m == d or r_s == d:
            result = 1
        else:
            result = 0
    
    print(result)   