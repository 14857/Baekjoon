# 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수 반환
def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        for j in range(2,i):
            if(i % j == 0):
                answer += 1
                break
    
    return answer