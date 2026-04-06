# 탐욕법(Greedy) -> 구명보트

def solution(people, limit):
    people.sort()
    
    left = 0              # 가장 가벼운 사람
    right = len(people)-1 # 가장 무거운 사람
    
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1   # 같이 태움
        
        right -= 1      # 무거운 사람은 무조건 태움
        answer += 1
    
    return answer