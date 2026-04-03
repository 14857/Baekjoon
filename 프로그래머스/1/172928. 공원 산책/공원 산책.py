# 하나씩 이동

def solution(park, routes):
    answer = []
    directions = ["E","W","S","N"]
    x_d = [0,0,1,-1]
    y_d = [1,-1,0,0]
    
    x,y = 0,0
    w = len(park[1])
    h = len(park)
    
    
    for i in range(h):
        for j in range(w):
            if(park[i][j] == "S"):
                x,y = i,j
    
    
    for i in routes:
        
        d, dist = i.split() # 방향
        dist = int(dist) # 이동거리
        
        dir_idx = directions.index(d)
    
        nx, ny = x, y

        for _ in range(dist):
            nx += x_d[dir_idx]
            ny += y_d[dir_idx]

            # 범위 벗어나면 실패
            if not (0 <= nx < h and 0 <= ny < w):
                break

            # 장애물 만나면 실패
            if park[nx][ny] == "X":
                break
        else:
            # 끝까지 성공했을 때만 이동
            x, y = nx, ny
            
    
    answer = [x,y]
    return answer