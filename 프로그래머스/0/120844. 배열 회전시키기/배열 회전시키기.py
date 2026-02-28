def solution(numbers, direction):
    answer = []
    answer = numbers
    
    if(direction == "left"):
        answer.append(numbers[0])
        answer.pop(0)
        
    elif(direction == "right"):
        answer.insert(0,numbers[-1])
        answer.pop()
        

    return answer