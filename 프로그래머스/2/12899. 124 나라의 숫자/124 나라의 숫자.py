# 연습문제 > 124 나라의 숫자

def solution(n):
    answer = ''
    
    rev_base = ''
    
    while n>0:
        n,mod = divmod(n, 3)
        
        if mod == 0:
            mod = 4
            n -= 1
        
        rev_base += str(mod)
    
    answer = rev_base[::-1] 
    
    answer.replace('0','1')
    answer.replace('1','2')
    answer.replace('2','4')
    
    return answer