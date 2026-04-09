# 괄호 회전하기
def check(s):
    stack = []

    for i in s:
        if(i in "[{("):
            stack.append(i)
        else:
            
            if not stack:
                return False
            
            if (i == "]" and stack[-1] == "["):
                stack.pop()
            elif (i == "}" and stack[-1] == "{"):
                stack.pop()
            elif (i == ")" and stack[-1] == "("):
                stack.pop()
            else:
                return False
            
    return (len(stack) == 0)
                
    
def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        
        if(check(s)):
            answer += 1
            
        s = s[1:] + s[0]
        
    
    return answer