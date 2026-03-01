# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값
def solution(numbers):
    answer = 0
    
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    
    return answer