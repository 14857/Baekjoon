# 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 반환

def solution(n, k):
    answer = 0
    
    answer = n*12000 + k*2000 - (n//10*2000)
    
    return answer