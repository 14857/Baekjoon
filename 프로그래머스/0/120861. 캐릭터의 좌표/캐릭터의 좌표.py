def solution(keyinput, board):
    answer = []
    
    keys = ["up", "down", "left", "right"]
    dire = [[0,1],[0,-1],[-1,0],[1,0]]
    x = 0
    y = 0
    
    for i in keyinput:

        # 우선 이동
        nx = x + dire[keys.index(i)][0]
        ny = y + dire[keys.index(i)][1]
        
        # 범위 확인
        if(abs(nx) <= board[0]//2 and abs(ny) <= board[1]//2):
            x = nx
            y = ny
            
    answer = [x,y]
    
    return answer