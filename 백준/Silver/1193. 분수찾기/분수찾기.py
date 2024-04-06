num = int(input())
line = 1

while (num > line):
    num = num - line
    line += 1

# 입력 값이 짝수 줄에 위치 -> 분자: +1, 분모: -1
if (line % 2 == 0):
    a = num
    b = line + 1 - num

# 입력 값이 홀수 줄에 위치 -> 분자: -1, 분모: +1
else:
    b = num
    a = line + 1 - num
    
    
print(f"{a}/{b}")