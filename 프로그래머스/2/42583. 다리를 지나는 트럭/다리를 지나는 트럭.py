# 스택/큐 > 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    
    while len(truck_weights) > 0:
        answer += 1
        bridge.pop(0)
        
        # 건널 수 있는 경우
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        
        # 건널 수 없는 경우
        else:
            bridge.append(0)
            
    answer += bridge_length

    return answer