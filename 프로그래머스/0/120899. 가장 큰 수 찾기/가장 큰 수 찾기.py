def solution(array):
    answer = []
    
    num = max(array)
    answer = [num, array.index(num)]
    
    return answer