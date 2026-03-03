def solution(s):
    answer = 0
    s_lst = s.split()
    nums = []
    
    
    for i in s_lst:
        if(i == "Z"):
            nums.pop()
        else:
            nums.append(int(i))
    answer = sum(nums)   
    print(nums)
    
    return answer