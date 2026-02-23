from math import ceil

def solution(n):
    answer = 1 
    
    while True:
        if(ceil(answer*6/n) == answer*6/n):
            break
        else:
            answer += 1
    
    
    return answer