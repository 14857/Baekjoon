def solution(cipher, code):
    answer = ''
    
    for i in range(0,len(cipher)-code+1,code):
        answer += cipher[i+code-1]
    
    return answer