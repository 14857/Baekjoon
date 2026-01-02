def solution(a, b, c):
    answer = (a+b+c)*(a*a + b*b + c*c)
    
    if (a == b):
        if(a == c): # 다같은 경우
            answer = (a+b+c)*(a*a + b*b + c*c)*(a*a*a + b*b*b + c*c*c)
    else:
        if(b != c and a != c):
            answer = (a+b+c)
    
    return answer