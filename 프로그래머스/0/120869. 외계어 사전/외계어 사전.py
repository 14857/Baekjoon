def solution(spell, dic):
    answer = 2
    
    for word in dic:
        
        temp = 1
        for alpabet in spell:
            if(alpabet not in word):
                temp = 2
        
        if(temp == 1):
            answer = 1
    
    return answer