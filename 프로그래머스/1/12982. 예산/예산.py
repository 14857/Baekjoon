# 그리디
def solution(d, budget):
    answer = 0
    cal = 0
    
    d.sort()
    
    for i in d:
        if(cal+i <= budget):
            cal += i
            answer += 1
    
    return answer