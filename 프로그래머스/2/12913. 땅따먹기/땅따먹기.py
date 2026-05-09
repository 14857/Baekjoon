# 연습문제 > 땅따먹기
# 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없다

def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    
    answer = max(land[-1])

    return answer