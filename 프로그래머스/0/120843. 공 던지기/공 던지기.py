# 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있다.
# k번째로 공을 던지는 사람의 번호는 무엇인지 반환

def solution(numbers, k):
    answer = 0
    
    cnt = 2*(k-1) % len(numbers)
    answer = numbers[cnt]
    
    return answer