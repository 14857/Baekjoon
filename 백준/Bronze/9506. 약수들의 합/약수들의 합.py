while True:
    nums = []
    n = int(input())
    
    if n == -1:
        break
    
    for i in range(1,n):
        if n%i == 0:
            nums.append(i)
    
    if n != sum(nums):
        ans = str(n) + " is NOT perfect."
        
    else:
        ans = str(n) + " = 1"
        for i in range (1,len(nums)):
            ans += " + " + str(nums[i])
    
    print(ans)