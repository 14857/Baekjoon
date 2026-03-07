def solution(before, after):
    answer = 1
    
    for i in before:
        if(before.count(i) != after.count(i)):
            answer = 0
    
    return answer