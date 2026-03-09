def solution(dots):
    answer = 0
    
    x = []
    y = []
    
    for i in dots:
        x.append(i[0])
        y.append(i[1])
        
    answer = (max(x) - min(x)) *(max(y) - min(y))
    
    return answer