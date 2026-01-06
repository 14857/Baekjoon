# 원소들의 곱과 합
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1
# 아닌 경우 0을 return

def solution(num_list):
    answer = 0
    
    mul = 1
    sum_s = sum(num_list) * sum(num_list)
    
    for i in num_list:
        mul *= i

    if (mul < sum_s):
        answer = 1
    
    
    return answer