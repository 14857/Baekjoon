# 떨어지는 순간 찾기
# 이중 for 문 -> 시간 초과 

def solution(prices):
    n = len(prices)
    answer = [0]*n
    stack = []
    
    for i in range(n):
        while (stack and prices[stack[-1]] > prices[i]):
            idx = stack.pop()
            answer[idx] = i - idx
        
        stack.append(i)
    
    # 끝까지 안 떨어진 애들 처리
    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx
    
    return answer