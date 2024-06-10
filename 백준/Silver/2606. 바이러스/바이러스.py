n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결 수
ab = []
connect = [i for i in range(1,n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    
    ab.append([x,y])

for i in range(m): 
    a = ab[i][0]
    b = ab[i][1]
    tmp = connect[b-1]
    
    for i in range(0,n):
        if connect[i] == tmp:
            connect[i] = connect[a-1]
        
print(connect.count(connect[0])-1)
