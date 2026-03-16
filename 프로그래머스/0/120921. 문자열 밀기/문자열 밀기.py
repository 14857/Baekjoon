# A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return

def solution(A, B):
    answer = -1
    temp = A
    
    # A와 B가 같은 경우
    if(A == B):
        answer = 0
    
    for i in range(len(temp)-1):
        temp = temp[-1] + temp[:len(temp)-1]
        
        if(temp == B):
            answer = i+1
            break
        
        # print(temp)
    
    return answer