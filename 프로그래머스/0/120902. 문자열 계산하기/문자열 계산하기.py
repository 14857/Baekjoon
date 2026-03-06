# 연산자 여러 개인 경우 고려
def solution(my_string):
    
    answer = 0
    my_list = my_string.split(" ")
    temp = '+'
    
    print(my_list)
    
    for i in my_list:
        if(i.isdigit() and temp == '-'):
            answer -= int(i)
        elif(i.isdigit() and temp == '+'):
            answer += int(i)
        else:
            temp = i
    
    return answer