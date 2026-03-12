# 3의 배수와 숫자 3을 사용 X
def solution(n):
    answer = 0
    lst = [0]*(n+1)
    cnt = 1
    
    for i in range(1,n+1):
        while(cnt % 3 == 0 or str(cnt).count('3') != 0):
            cnt += 1           
        lst[i] = cnt
        cnt += 1

    
    answer = lst[n]
    
    return answer