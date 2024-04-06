white = [1,1,2,2,2,8]
result = [0]*6

black = list(map(int,input().split()))

for i in range(6):
    result[i] = white[i] - black[i]

print(*result)