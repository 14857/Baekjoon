# 연습문제 > 행렬의 곱셈

def solution(arr1, arr2):
    
    n = len(arr1) # 행
    m = len(arr2[0]) # 열
    k = len(arr2)
    
    answer = [[0]*m for _ in range(n)]
    
    for i in range(n): # arr1의 행 선택
        for j in range(m): # arr2의 열 선택
            for t in range(k): # 행과 열을 곱해서 누적
                answer[i][j] += arr1[i][t] * arr2[t][j]
    
    return answer