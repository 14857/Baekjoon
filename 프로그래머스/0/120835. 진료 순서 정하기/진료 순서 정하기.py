def solution(emergency):
    answer = []
    turns = sorted(emergency, reverse = True)

    for i in emergency:
        answer.append(turns.index(i) + 1)
    
    return answer