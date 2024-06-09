bingo = []
ans = []
count = 0
n = 0

def check(count):
    for i in range(5):
        if bingo[i] == [0] * 5:
            count += 1
    for i in range(5):
        if all(bingo[j][i] == 0 for j in range(5)):
            count += 1

    if all(bingo[i][i] == 0 for i in range(5)):
        count += 1
    
    if all(bingo[i][4 - i] == 0 for i in range(5)):
        count += 1
    return count



for _ in range(5):
    bingo.append(list(map(int,input().split())))
    
for _ in range(5):
    a,b,c,d,e = map(int,input().split())
    ans.append(a)
    ans.append(b)
    ans.append(c)
    ans.append(d)
    ans.append(e)
    
for i in range(25):
    for x in range(5):
        for y in range(5):
            if ans[i] == bingo[x][y]:
                bingo[x][y] = 0
                n += 1
    
    if n >= 12:
        if check(count) >= 3:
            print(i+1)
            break