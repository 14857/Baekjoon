board = []
count = 0
for _ in range(8):
    board.append(list(input()))
    
for i in range(0,8,2): # 흰색으로 시작하는 줄
    for j in range(0,8,2):
        if board[i][j] == 'F':
            count += 1
    
for i in range(1,8,2):
    for j in range(1,8,2):
        if board[i][j] == 'F':
            count += 1

print(count)