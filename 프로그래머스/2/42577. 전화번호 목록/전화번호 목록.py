# 해시 > 전화번호 목록
# 접두어인 경우 사전상 옆에 위치

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if(phone_book[i+1].startswith(phone_book[i])):
            answer = False
    
    return answer