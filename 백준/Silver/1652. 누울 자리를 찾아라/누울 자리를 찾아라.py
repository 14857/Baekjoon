n = int(input())
room = []

for _ in range(n):
    tmp = list(input())
    room.append(tmp)

row = 0
col = 0
        
for i in range(n):
    tmpa, tmpb = 0, 0
    for j in range(n):
        if room[i][j] == '.':
            tmpb += 1
        else:
            tmpb = 0 # 연속이 아니면 초기화
        if tmpb == 2: # 연속이면 해당 row count (가로)
            row += 1

        if room[j][i] == '.':
            tmpa += 1
        else:
            tmpa = 0 # 연속이 아니면 초기화
        if tmpa == 2: # 연속이면 해당 col count (세로)
            col += 1

print(row, col, end = ' ')