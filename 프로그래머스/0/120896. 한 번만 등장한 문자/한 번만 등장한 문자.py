# s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열 반환

def solution(s):
    answer = ''
    nums = []
    dic = {}
    
    for i in s:
        if(i in dic):
            dic[i] += 1
        else:
            dic[i] = 1
    
    for key in dic.keys():
        if(dic[key] == 1):
            nums.append(key)
            
    nums.sort()
    answer = "".join(nums)

    return answer