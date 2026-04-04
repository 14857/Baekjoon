# 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse = True)
    
    for i in range (len(A)):
        answer += A[i] * B[i]
    
    return answer