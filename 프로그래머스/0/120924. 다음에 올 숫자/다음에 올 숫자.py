def solution(common):
    answer = 0
    
    # 등차수열인 경우
    if(common[2] - common[1] == common[1] - common[0]):
        d = common[2] - common[1]
        answer = common[-1] + d
        
    # 등비수열인 경우
    else:
        n = common[2] / common[1]
        answer = common[-1] * n
    
    return answer