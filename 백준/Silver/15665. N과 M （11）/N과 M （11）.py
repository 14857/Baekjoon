# 백트래킹 사용하기

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    
    num = 0
    
    for i in range(n):
        if num != nums[i]:
            temp.append(nums[i])
            num = nums[i]
            dfs()
            temp.pop()

dfs()