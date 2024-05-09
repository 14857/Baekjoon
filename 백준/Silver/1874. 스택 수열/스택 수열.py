n = int(input())
count = 1
stack = []
ans = []
exist = 1

# 수열 개수
for i in range(n):
    
    num = int(input())
    
    # push 구현
    while count <= num: 
        stack.append(count)
        ans.append('+')
        count += 1
    
    # pop 구현
    if stack[-1] == num:
        ans.append('-')
        stack.pop()
    
    else:
        exist = 0
        

if exist == 0:
    print("NO")

else:
    for i in ans:
        print(i)