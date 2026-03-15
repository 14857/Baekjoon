# 정수 n을 기준으로 n과 가까운 수부터 정렬
# n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치

def solution(numlist, n):
    answer = []
    
    numlist.sort(key=lambda x: (abs(x - n),-x))

                 
    answer =  numlist
    return answer