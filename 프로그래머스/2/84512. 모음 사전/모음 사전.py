# 완전탐색 > 모음사전
# 이 단어가 사전에서 몇 번째 단어인지 return
# 각 자리의 가중치 : [781, 156, 31, 6, 1]

def solution(word):
    answer = 0
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]
    
    for i, ch in enumerate(word):
        idx = vowels.index(ch)
        answer += idx * weights[i] + 1
        
    return answer