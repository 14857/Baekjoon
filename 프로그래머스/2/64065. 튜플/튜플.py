# 2019 카카오 개발자 겨울 인턴십 > 튜플

def solution(s):
    answer = []
    
    s = s[2:-2]
    arr = s.split("},{")
    
    arr.sort(key=len)
    
    for group in arr:
        for x in group.split(","):
            x = int(x)
            if x not in answer:
                answer.append(x)
                
    return answer