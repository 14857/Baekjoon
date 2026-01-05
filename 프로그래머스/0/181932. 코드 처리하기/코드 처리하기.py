def solution(code):
    answer = ''
    mode = 0
    
    for i in range (0,len(code)):
        if code[i] == "1":
            mode = 0 if mode == 1 else 1   
        else:
            if (i %2 == 0 and mode == 0) or(i %2 == 1 and mode == 1):
                answer+=(code[i])
    if len(answer) == 0:
        answer = "EMPTY"
    
    return answer


