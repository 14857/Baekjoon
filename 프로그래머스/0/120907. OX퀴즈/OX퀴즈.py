def solution(quiz):
    answer = []
    
    for i in quiz:
        temp = i.split(" ")
        num1 = int(temp[0])
        num2 = int(temp[2])
        ans = int(temp[4])
        
        if(temp[1] == '+'):
            if(num1 + num2 == ans):
                answer.append("O")
            else:
                answer.append("X")
                
        elif(temp[1] == '-'):
            if(num1 - num2 == ans):
                answer.append("O")
            else:
                answer.append("X")
    
    return answer