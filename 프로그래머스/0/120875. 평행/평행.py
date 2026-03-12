# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 반환
# 기울기가 동일한지 확인

def solution(dots):
    answer = 0
    
    #(0 1, 2 3) (0 2, 1 3) (0 3, 1 2)
    
    a = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    b = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    
    m = (dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0])
    n = (dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0])
    
    i = (dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0])
    j = (dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
    
    
    if(a == b or m == n or i == j):
        answer = 1
    
    
    return answer