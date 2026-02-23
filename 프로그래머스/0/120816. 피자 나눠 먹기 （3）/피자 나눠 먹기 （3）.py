# n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 

from math import ceil
def solution(slice, n):
    answer = 0
    answer =  ceil(n/slice)
    
    return answer