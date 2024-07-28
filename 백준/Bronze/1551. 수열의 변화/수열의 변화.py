# 수열을 이루고 있는 수는 절댓값이 100보다 작거나 같은 정수

n,k = map(int,input().split())
lst = list(map(int,input().split(",")))
ans = [i for i in lst]

for _ in range(k):
    ans = []
    for i in range(len(lst)-1):
        num = lst[i+1]-lst[i]
        ans.append(num)
            
    lst = ans
    
for i in range(len(ans)):
    ans[i] = str(ans[i])

print(",".join(ans))