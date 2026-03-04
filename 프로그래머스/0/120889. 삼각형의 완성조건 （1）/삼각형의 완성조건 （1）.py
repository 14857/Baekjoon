def solution(sides):
    answer = 0
    
    longest = max(sides)
    sides.remove(longest)
    
    if(longest < sides[0]+sides[1]):
        answer = 1
    else:
        answer = 2
    
    return answer