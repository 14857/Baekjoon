def solution(my_string, num1, num2):
    answer = ''
    s_lst = list(my_string)
    
    temp = s_lst[num1]
    s_lst[num1] = s_lst[num2]
    s_lst[num2] = temp
    
    answer = "".join(s_lst)
    
    return answer