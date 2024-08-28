# 테스트케이스의 개수 t / 현재 위치 x / 목표 위치 y 
# 지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램
# y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년

t = int(input())

for _ in range(t):
    x,y = map(int,input().split())
    
    d = y-x
    tmp = 0 # 이동 거리
    cnt = 0 # 공간 장치 이동 횟수
    moving = 0 # 반복 횟수
    
    while tmp<d:
        cnt += 1
        if cnt %2 != 0:
            moving += 1
        tmp += moving
        
    print(cnt)