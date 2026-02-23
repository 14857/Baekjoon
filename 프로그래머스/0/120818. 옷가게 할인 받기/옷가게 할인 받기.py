# 소수점 이하를 버린 정수 반환

from math import floor

def solution(price):
    answer = 0
    
    if (price >= 500000):
        answer = floor(price * 0.8)
    elif (price >= 300000):
        answer = floor(price * 0.9)
    elif (price >= 100000):
        answer = floor(price * 0.95)
    else:
        answer = price
    
    return answer