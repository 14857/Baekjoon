import sys
input = sys.stdin.readline

ans = {}

n = int(input())
n_lst = list(map(int,input().split()))

m = int(input())
m_lst = list(map(int,input().split()))

for i in n_lst:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1
    
for i in m_lst:
    if i in ans:
        print(ans[i], end = ' ')
    else:
        print(0,end = ' ')