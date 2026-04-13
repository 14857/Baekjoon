# 연습문제 > 롤케이크 자르기
# 롤케이크를 공평하게 자르는 방법의 수

# 슬라이싱 -> 시간초과 발생
# 딕셔너리 사용

from collections import Counter

def solution(topping):
    answer = 0
    
    right = Counter(topping)
    left = set()
    
    for k in topping:
        left.add(k)
        right[k] -= 1 
        
        if(right[k] == 0):
            del right[k]
            
        if(len(left) == len(right)):
            answer += 1
    
    return answer