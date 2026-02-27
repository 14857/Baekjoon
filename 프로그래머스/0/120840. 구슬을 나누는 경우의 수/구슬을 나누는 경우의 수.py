# balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수
import math

def solution(balls, share):
    answer = 0
    
    answer = math.factorial(balls) / math.factorial(balls-share) / math.factorial(share)
    
    
    return answer