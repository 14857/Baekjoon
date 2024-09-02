# 은하수 지도, 출발점, 도착점이 주어졌을 때 최소의 행성계 진입/이탈 횟수를 구하는 프로그램
# 테스트 케이스의 개수 T / 출발점 (x1, y1) 도착점 (x2, y2) /  행성계의 개수 n / 행성계의 중점과 반지름 (cx, cy, r)

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = list(map(int, input().split()))
    n = int(input())
    
    count = 0
    
    for _ in range(n):
        cx, cy, cr = map(int, input().split())
        
        d1 = (x1 - cx)**2 + (y1 - cy)**2
        d2 = (x2 - cx)**2 + (y2 - cy)**2

        if cr**2 > d1 and cr**2 < d2:
            count += 1
            
        elif cr**2 > d2 and cr**2 < d1:
            count += 1
            
    print(count)