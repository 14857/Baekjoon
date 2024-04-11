N = int(input())
N_lst =  set(map(int,input().split()))

M = int(input())
M_lst = list(map(int,input().split()))

for a in M_lst:
    if a in N_lst:
        print(1)
    
    else:
        print(0)