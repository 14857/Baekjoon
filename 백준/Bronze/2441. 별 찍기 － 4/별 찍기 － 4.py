num = int(input())

for i in range(num,0,-1):
    line = ' '*(num-i) + '*'*i
    print(line)