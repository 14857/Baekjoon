def solution(array):
    answer = 0
    
    array.sort()
    answer = array[(len(array)-1)//2]
    
    return answer