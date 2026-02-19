from math import ceil

def solution(progresses, speeds):
    answer = []
    fin = []
    
    # 기능별 걸리는 시간
    for i in range(len(progresses)):
        fin.append(ceil((100-progresses[i])/speeds[i]))
    
    # 각 배포별 기능 수 계산
    while(len(fin) != 0):
        start = fin[0]
        count = 1
        i = 1
        
        while(i<len(fin) and fin[i] <= start):
            count += 1
            i += 1
        
        answer.append(count)
        
        fin = fin[count:]
    
    return answer