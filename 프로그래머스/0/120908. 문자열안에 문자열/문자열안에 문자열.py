# str1 안에 str2가 있다면 1을 없다면 2 반환

def solution(str1, str2):
    answer = 2
    
    if (str2 in str1):
        answer = 1
    
    return answer