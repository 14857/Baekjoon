def solution(score):
    answer = []
    
    lst = []
    for i in score:
        lst.append(sum(i)/2)   
    lst.sort(reverse = True)

    for i in score:
        answer.append(lst.index(sum(i)/2) + 1)
        
    return answer