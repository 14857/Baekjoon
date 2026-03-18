# total // num이 중앙값
# 연속된 수는 중앙값 기준으로 대칭 -> 시작값 찾기

def solution(num, total):
    answer = [0]
    
    start = total // num - (num - 1) // 2
    
    answer = [start + i for i in range(num)]
        
    return answer