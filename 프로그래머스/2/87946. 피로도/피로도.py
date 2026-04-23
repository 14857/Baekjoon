# "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
# "소모 피로도"는 던전을 탐험한 후 소모되는 피로도
# 유저가 탐험할수 있는 최대 던전 수를 return

# 완전탐색 -> 모든 경우의 수 계산하기

from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for case in permutations(dungeons):
        fatigue = k
        cnt = 0

        for need, cost in case:
            if fatigue >= need:
                fatigue -= cost
                cnt += 1
            else:
                break
    
        answer = max(answer, cnt)
    
    return answer