 # n개의 카드 중 m장의 숫자가 적혀있는 카드를 가지고 있는지 구하는 프로그램
ans = []
 
n = int(input())
n_lst = set(map(int,input().split()))
 
m = int(input())
m_lst = list(map(int,input().split()))


for i in m_lst:
    if i in n_lst:
        ans.append(1)
    else:
        ans.append(0)
        
print(*ans)