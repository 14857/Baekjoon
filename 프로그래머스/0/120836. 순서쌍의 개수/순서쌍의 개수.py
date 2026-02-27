# 두 숫자의 곱이 n인 자연수 순서쌍의 개수 반환

def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if(n % i == 0):
            answer += 1
            
    return answer