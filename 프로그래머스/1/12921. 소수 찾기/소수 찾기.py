import math
# 소수 판별 함수 (소수인 경우 1, 아닌 경우 0)
def check(num):    
    if(num == 1):
        return 0
    
    for i in range(2,int(math.sqrt(num))+1):
        if(num % i == 0): # 소수 아님
            return 0
        
    return 1
      

def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        answer += check(i)
    
    return answer