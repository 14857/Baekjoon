# 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지 계산 후 반환

def solution(hp):
    answer = 0

    # 장군개미
    answer += hp // 5
    hp = hp % 5
    
    # 병정개미
    answer += hp // 3
    hp = hp % 3
    
    # 일개미
    answer += hp
    
    return answer