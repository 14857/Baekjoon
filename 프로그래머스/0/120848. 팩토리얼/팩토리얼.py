# i! ≤ n을 만족하는 가장 큰 정수 i 반환

def solution(n):
    answer = 0
    lst = [0,1]
    cnt = 2
    
    while(lst[-1] <= n):
        lst.append(lst[-1]*cnt)
        cnt += 1
    
    answer = len(lst) - 2
    
    return answer