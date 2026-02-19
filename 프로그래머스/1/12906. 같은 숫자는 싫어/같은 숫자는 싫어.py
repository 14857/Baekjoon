# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

def solution(arr):
    answer = []
    
    for i in arr:
        if(len(answer) == 0 or answer[-1] != i):
            answer.append(i)
    
    return answer