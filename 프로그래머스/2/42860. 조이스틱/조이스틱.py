# 탐욕법(Greedy) > 조이스틱

def solution(name):
    answer = 0
    
    # 각 문자마다 위/아래 최소 이동 더하기
    for c in name:
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    
    # 위치
    move = len(name) - 1

    for i in range(len(name)):
        next = i + 1

        while next < len(name) and name[next] == 'A':
            next += 1
        
        num1 = i * 2 + (len(name) - next)
        num2 = i + 2 * (len(name) - next)

        move = min(move, num1, num2)

    answer += move
    
    return answer