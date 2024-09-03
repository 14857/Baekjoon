# 첫 번째 자연수 : 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
# 두 번째 자연수 : 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리
# 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이
# 색종이가 붙은 검은 영역의 넓이를 출력
n = int(input())

array = [[0] * 100 for _ in range(100)]
ans = 0

for _ in range(n): 
    y, x = map(int, input().split())  

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            array[i][j] = 1

for k in range(100):
    ans += array[k].count(1)

print(ans)