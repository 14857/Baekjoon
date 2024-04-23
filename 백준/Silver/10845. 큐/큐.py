# 정수를 저장하는 큐를 구현 -> 각종 명령 처리

# 명령의 수 N
import sys

que = []

N = int(sys.stdin.readline())

for _ in range(N):
    
    s = sys.stdin.readline().split()
    
    if s[0] == 'pop': # pop
        if (len(que) == 0):
            print(-1)
        else:
            print(que.pop(0))       

    elif s[0] == 'size': # size
        print(len(que))
    
    elif s[0] == 'empty': # empty
        if len(que) == 0:
            print(1)
        else:
            print(0)            
            
    # top
    elif s[0] == 'front': # front
        if (len(que) == 0):
            print(-1)
        else:
            print(que[0])
            
    elif s[0] == 'back': # back
        if (len(que) == 0):
            print(-1)
        else:
            print(que[-1])
    
    # push
    else:
        x = int(s[1])
        que.append(x)