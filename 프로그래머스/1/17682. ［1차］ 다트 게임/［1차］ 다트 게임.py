# Single(S), Double(D), Triple(T) -> (점수^1 , 점수^2 , 점수^3 )으로 계산
# re.findall : 문자열에서 패턴에 맞는 것들 전부 찾아서 리스트로 반환
# \d+ = 숫자 1개 이상 / [SDT] = S 또는 D 또는 T / [*#] * 또는 #

import re

def solution(dartResult):
    
    tokens = re.findall(r'\d+|[SDT]|[*#]', dartResult)
    scores = []
    
    i = 0
    while i < len(tokens):
        num = int(tokens[i])
        i += 1
        
        bonus = tokens[i]
        i += 1
        
        if bonus == 'S':
            num **= 1
        elif bonus == 'D':
            num **= 2
        else:
            num **= 3
        
        # 스타상, 아차상 판별
        if (i < len(tokens) and tokens[i] in ['*', '#']):
            if tokens[i] == '*':
                num *= 2
                if scores:
                    scores[-1] *= 2
            else:
                num *= -1
            i += 1
        
        scores.append(num)
    
    return sum(scores)