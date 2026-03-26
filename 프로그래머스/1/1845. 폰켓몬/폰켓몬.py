# N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 
# 그때의 폰켓몬 종류 번호의 개수를 return

def solution(nums):
    answer = 0
    
    # N/2 마리 
    cnt = len(nums)//2
    print(cnt)
    
    nums_set = set(nums)
    
    if(len(nums_set) <= cnt):
        answer = len(nums_set)
    else:
        print(cnt,len(nums_set))
        answer = min(cnt,len(nums_set))
    
    return answer