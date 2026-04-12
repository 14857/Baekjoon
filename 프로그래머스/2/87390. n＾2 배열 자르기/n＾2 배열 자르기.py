# 패턴 : arr[i][j] = max(i+1, j+1)

def solution(n, left, right):
    answer = []
    
    for k in range(left, right+1):
        row = k // n
        col = k % n
        
        answer.append(max(row+1, col+1))
    
    return answer