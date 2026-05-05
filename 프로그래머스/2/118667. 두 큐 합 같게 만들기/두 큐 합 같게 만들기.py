# 2022 KAKAO TECH INTERNSHIP > 두 큐 합 같게 만들기
# 각 큐의 원소 합이 같도록 -> 필요한 작업의 최소 횟수 
# 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행
# 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 

from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2
    
    # 전체 합이 홀수면 불가능
    if (total % 2 == 1):
        return -1
    
    target = total // 2
    
    limit = (len(queue1) + len(queue2)) * 2  # 무한 루프 방지
    
    while answer <= limit:
        if sum1 == target:
            return answer
        
        if sum1 > target:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            sum2 -= x
            sum1 += x
        
        answer += 1
    
    return -1
