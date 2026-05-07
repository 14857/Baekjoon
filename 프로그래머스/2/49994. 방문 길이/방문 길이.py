# Summer/Winter Coding(~2018) > 방문 길이
# 좌표가 아니라 길 자체를 저장하기

def solution(dirs):
    answer = 0
    x, y = 0, 0
    visited = set()
    
    move = { 'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    
    for d in dirs:
        dx,dy = move[d]
        nx = x + dx 
        ny = y + dy
        
        # 범위를 넘어서는 경우
        if(nx < -5 or nx > 5 or ny < -5 or ny > 5):
            continue
        
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            answer += 1
        
        x, y = nx, ny

    return answer