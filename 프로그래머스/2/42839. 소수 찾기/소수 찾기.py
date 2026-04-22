# 완전탐색 > 소수 찾기

from itertools import permutations

# 소수 판별 함수
def chk(num):
    if(num <= 1):
        return 0
    
    for i in range(2,num):
        if(num % i == 0):
            return 0    
    return 1
    
    
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    nums = set()
    
    # 만들 수 있는 수
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            nums.add(int("".join(j)))
            
    # 소수 판별
    for i in nums:
        answer += chk(i)
    
    return answer