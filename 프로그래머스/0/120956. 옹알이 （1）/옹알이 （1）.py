def solution(babbling):
    answer = 0
    
    words = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        temp = i
        
        for w in words:
            if(w in temp):
                temp = temp.replace(w," ")
        
        if not temp.strip():
            answer += 1

    return answer