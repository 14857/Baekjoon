# 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열 반환

def solution(money):
    answer = []
    
    # 최대로 마실 수 있는 아메리카노 잔 수
    answer.append(money // 5500)
    
    # 남는 돈
    answer.append(money % 5500)
    
    return answer