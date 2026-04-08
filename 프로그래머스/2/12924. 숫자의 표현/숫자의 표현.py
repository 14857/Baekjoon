# 자연수 n을 연속한 자연수들로 표현 하는 방법 == 홀수 약수 개수

def solution(n):
    answer = 0
    
    
    for i in range(1,n+1,2):
        if(n%i == 0):
            answer += 1
    
    return answer