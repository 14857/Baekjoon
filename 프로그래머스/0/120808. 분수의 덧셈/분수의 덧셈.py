# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열

import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    denom = denom1 * denom2
    numer = (numer1*denom2) + (numer2*denom1)
    
    # 최대 공약수
    gcd = math.gcd(numer,denom)
    
    answer.append(numer//gcd)
    answer.append(denom//gcd) 
    
    return answer