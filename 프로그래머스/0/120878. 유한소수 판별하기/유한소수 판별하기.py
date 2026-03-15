# a/b가 유한소수이면 1을, 무한소수라면 2를 return

import math

def solution(a, b):
    answer = 0
    
    g = math.gcd(a, b)    
    b = b // g # 기약분수의 분모로만 판별 가능

    while b % 2 == 0:
        b = b // 2

    while b % 5 == 0:
        b = b // 5

    if b == 1:
        answer = 1
    else:
        answer = 2
    
    return answer