def solution(order):
    answer = 0
    order = str(order)
    
    answer = order.count('3') + order.count('6') + order.count('9')
    
    return answer