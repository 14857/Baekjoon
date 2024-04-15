# 명령의 수 N
import sys

lst = []

N = int(sys.stdin.readline())

for _ in range(N):
    
    s = sys.stdin.readline().split()
    
    if s[0] == '2':
        if (len(lst) == 0):
            print(-1)
        else:
            print(lst.pop())       
    

    elif s[0] == '3':
        print(len(lst))
    
    elif s[0] == '4':
        if len(lst) == 0: # 비어있는 경우
            print(1)
        else:
            print(0)            
            
    # top
    elif s[0] == '5':
        if (len(lst) == 0):
            print(-1)
        else:
            print(lst[-1])
    
    # 1
    else:
        x = int(s[-1])
        lst.append(x)
        