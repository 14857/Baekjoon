numlist = []
ans = 0
ans_a = 1
ans_b = 1

for i in range(9):
    nums = list(map(int,input().split()))
    numlist.append(nums)
    
for a in range(9):
    for b in range(9):
        if (ans < numlist[a][b]):
            ans = numlist[a][b]
            ans_a = a+1
            ans_b = b+1
        
print(ans)
print(ans_a, ans_b)