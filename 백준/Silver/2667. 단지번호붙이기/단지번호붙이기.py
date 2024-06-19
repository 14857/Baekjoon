# 첫 번째 줄에는 총 단지수를 출력
#  각 단지내 집의 수를 오름차순으로 정렬

def dfs(x,y):
    
    global count
    
    if x<0 or x>= n or y<0 or y>=n: # 그래프의 범위를 벗어나는 경우
        return False
    
    else:
        if graph[x][y] == 1: # 주거중
            count += 1
            graph[x][y] = 0 # 방문 처리
            
            for i in range(4):
                dfs(x+dx[i], y+dy[i])
            return True
        return False
    
            
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = [] # 지도
num = [] # 단지내 집의 수

count = 0 # # 단지내 집의 수 count 변수
total = 0 # 총 단지 수

n = int(input()) # 지도의 크기

for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(count)
            total += 1
            count = 0

num.sort()

print(total) # 총 단지 수

for i in num:
    print(i)
               