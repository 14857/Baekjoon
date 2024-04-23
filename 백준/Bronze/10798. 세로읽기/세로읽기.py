board = []
length = []
ans = ''

for _ in range(5):
    s = input()
    board.append(s)
    length.append(len(s))

for j in range(max(length)):
    for k in range(5):
        if j < length[k]:
            ans += board[k][j]

print(ans)