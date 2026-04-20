# 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시
# 각 도시 이름은 대소문자 구분을 하지 않는다.

def solution(cacheSize, cities):
    answer = 0
    stack = [0] * cacheSize
    
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        city = city.lower()
        
        # cache hit인 경우 -> +1
        if(city in stack):
            stack.remove(city)
            stack.append(city)
            answer += 1
        
        # cache miss인 경우
        else:
            # stack 에서 LRU 제거 
            if len(stack) >= cacheSize:
                stack.pop(0)
                
            stack.append(city)
            answer += 5         
    
    return answer