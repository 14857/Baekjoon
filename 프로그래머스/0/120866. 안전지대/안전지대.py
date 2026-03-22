# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수 반환
# 위험지역이 겹치는 경우도 고려

def solution(board):
    
    n = len(board)
    answer = n*n
    check = [[0]*n for i in range(n)]
    
    print(check)
    
    directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),  (0,0),  (0, 1),
    (1, -1),  (1, 0), (1, 1)
]
    
    # 위험 지역 표시
    for i in range(n):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for dx, dy in directions:
                    nx = i + dx
                    ny = j + dy

                    if 0 <= nx < n and 0 <= ny < n:
                        check[nx][ny] = 1
    print(check)
    
    for i in check:
        answer -= i.count(1)

        
        
    # 안전한 지역의 칸 수 반환

    
    
    
    return answer