n = int(input())

student = []
ans = [0]*n

for _ in range(n):
    student.append(list(map(int,input().split())))

for i in range(n):
    count = 0
    for j in range(n):
        if student[i][0]<student[j][0] and student[i][1]<student[j][1]:
            count += 1
    
    ans[i] = count+1

print(*ans)