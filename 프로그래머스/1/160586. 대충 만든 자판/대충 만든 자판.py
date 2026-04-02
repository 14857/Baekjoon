def solution(keymap, targets):
    answer = []
    dict = {}
    
    for i in keymap:
        for j in i:
            if j not in dict:
                dict[j] = i.index(j) +1
            else:
                dict[j] = min(dict[j], i.index(j) +1)
    
    print(dict)
    
    for i in targets:
        cnt = 0
        flag = True
        
        for j in i:
            if j not in dict:
                flag = False
                break
            cnt += dict[j]

        if flag:
            answer.append(cnt)
        else:
            answer.append(-1)
        
           
        
    return answer