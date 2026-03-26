# 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
def solution(s):
    answer = False

    
    if(s.count('p') + s.count('P')  == s.count('y') + s.count('Y')):
        answer = True
       
    
    
    return answer