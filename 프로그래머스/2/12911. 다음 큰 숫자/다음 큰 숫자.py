# 다음 큰 숫자

def solution(n):
    answer = 0
    
    cnt = bin(n).count('1')
    print(cnt)
    
    answer = n+1
    while (True):
        if(bin(answer).count('1') == cnt):
            break
        answer += 1
        
    return answer