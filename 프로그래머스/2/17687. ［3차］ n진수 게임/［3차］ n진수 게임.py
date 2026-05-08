# 2018 KAKAO BLIND RECRUITMENT > [3차] n진수 게임
# 자신이 말해야 하는 숫자를 스마트폰에 미리 출력
# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p

# 10진수 -> n진수 문자열
def convert(num,n):
    digits = "0123456789ABCDEF"
        
    if num == 0:
        return "0"
        
    result = ""
        
    while num > 0:
        result = digits[num % n] + result
        num //= n
            
    return result

def solution(n, t, m, p):
    
    numbers = ""
    num = 0
    
    # 필요한 길이만큼 n진수 문자열 이어붙이기
    while len(numbers) < t * m:
        numbers += convert(num,n)
        num += 1
    
    answer = ""
    
    # 튜브가 말해야 하는 문자만 추출
    for i in range(t):
        answer += numbers[(p - 1) + i * m]
    
    return answer