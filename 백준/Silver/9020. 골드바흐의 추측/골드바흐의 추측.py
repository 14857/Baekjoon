# 4 ≤ n ≤ 10,000

nums = set() # 서로소 리스트

for i in range(2,10000):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count += 1
    
    if count == 0:
        nums.add(i)

t = int(input())

for _ in range(t):
    n = int(input())
    
    dif = 10000
    for i in nums:
        if (n-i) in nums:
            if abs(i-n+i) < dif:
                dif = abs(i-n+i)
                ans1 = min(i,n-i)
                ans2 = max(i,n-i)
    
    print(ans1,ans2)