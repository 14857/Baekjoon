# 명령의 수 N
import sys

lst = []

N = int(sys.stdin.readline())

for _ in range(N):
    
    s = sys.stdin.readline().split()
    
    # pop
    if s[0] == 'pop':
        if (len(lst) == 0):
            print(-1)
        else:
            print(lst.pop())
            #print(lst[-1])
            #lst.remove(lst[-1])          
    
    # size
    elif s[0] == 'size':
        print(len(lst))
    
    # empty
    elif s[0] == 'empty':
        if len(lst) == 0: # 비어있는 경우
            print(1)
        else:
            print(0)            
            
    # top
    elif s[0] == 'top':
        if (len(lst) == 0):
            print(-1)
        else:
            print(lst[-1])
    
    # push
    else:
        x = int(s[-1])
        lst.append(x)
        