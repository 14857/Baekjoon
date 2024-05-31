# 명령의 수 N
import sys

ans = set()

N = int(sys.stdin.readline())

for _ in range(N):
    
    s = sys.stdin.readline().split()

    if s[0] == 'add':
        if s[1] not in ans:
            ans.add(s[1])          
    
    elif s[0] == 'remove':
        if s[1] in ans:
            ans.remove(s[1])
    
    # empty
    elif s[0] == 'check':
        if s[1] in ans:
            print(1)
        else:
            print(0)
            
    elif s[0] == 'toggle':
        if s[1] in ans:
            ans.remove(s[1])
        else:
            ans.add(s[1])   

    elif s[0] == 'all':
        ans = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    
    elif s[0] == 'empty':
        ans = set()
