# n이 제곱수라면 1을 아니라면 2를 return
import math
def solution(n):
    answer = 2
    
    if(int(math.sqrt(n)) == math.sqrt(n)):
        answer = 1

    return answer