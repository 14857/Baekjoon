# array에 들어있는 정수 중 n과 가장 가까운 수를 반환
# 가장 가까운 수가 여러 개일 경우 더 작은 수

def solution(array, n):
    answer = 0
    cal = []
    
    array.sort()
    
    for i in array:
        cal.append(abs(i-n))
        
    answer = array[cal.index(min(cal))]
    
    
    return answer