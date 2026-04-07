# 코딩테스트 연습 > 스택/큐 > 올바른 괄호
# replace("()","") -> 시간 초과
# 스택 사용

def solution(s):
    stack = []
    answer = True
    
    for ch in s:
        if(ch == "("):
            stack.append(ch)
        else:
            if not stack:
                answer = False
                break
                
            stack.pop()
    
    if(len(stack) != 0):
        answer = False
        
    return answer