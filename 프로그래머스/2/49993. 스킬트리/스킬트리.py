# Summer/Winter Coding(~2018) > 스킬트리

def solution(skill, skill_trees):
    answer = 0
    possible = []

    # 가능한 스킬 순서
    for i in range(1,len(skill)+1):
        possible.append(skill[:i])
    
    
    for tree in skill_trees:
        filtered = ''
        
        for c in tree:
            if(c in skill):
                filtered += c
        
        if filtered in possible or filtered == '':
            answer += 1

    
    return answer