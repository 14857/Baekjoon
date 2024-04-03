num = [0]*30

for _ in range(28):
    a = int(input())
    num[a-1] = 1


for i in range(30):
    if num[i] == 0:
        print(i+1)