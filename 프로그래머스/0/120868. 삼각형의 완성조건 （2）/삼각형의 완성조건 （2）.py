# 나머지 한 변이 될 수 있는 정수의 개수를 return
def solution(sides):
    answer = 0
    candidate = set()
    
    # max(sides)가 가장 큰 변의 길이인 경우
    for i in range(0,max(sides)):
        if(i + min(sides) > max(sides)):
            candidate.add(i)
    
    # 나머지 한 변이 가장 긴 변인 경우
    for i in range(max(sides), sum(sides)):
        candidate.add(i)
    
    answer = len(candidate)
    
    return answer