# 지폐를 접을 때는 항상 길이가 긴 쪽을 반으로 접습니다.
# 접기 전 길이가 홀수였다면 접은 후 소수점 이하는 버립니다.
# 접힌 지폐를 그대로 또는 90도 돌려서 지갑에 넣을 수 있다면 그만 접습니다.

def solution(wallet, bill):
    answer = 0  
    
    while(True):
        
        if(min(bill) <= min(wallet) and max(bill) <= max(wallet)):
            break
        
        if(bill[0] > bill[1]):
             bill[0] = bill[0] // 2     
        else:
            bill[1] = bill[1] // 2
            
        answer += 1
    
    
    return answer