# max(반복가능한객체, key=기준함수) : 각 요소를 어떤 기준으로 비교할지 정한다

def solution(array):
    answer = 0
    dic = {}
    
    for i in array:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    answer = max(dic, key = dic.get)
    
    max_value = max(dic.values())
    max_keys = [k for k, v in dic.items() if v == max_value]
    
    if(len(max_keys) >= 2):
        answer = -1
    else:
        answer =  max_keys[0]


    return answer