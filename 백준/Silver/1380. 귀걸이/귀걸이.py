#  한 줄에 귀걸이를 압수당한 여학생의 수, n (1 ≤ n ≤ 100)
# 다음 n줄에 걸쳐 여학생들의 이름(최대 60자)
#  테스트 케이스 번호(x)는 1부터 시작

ans = []

t = int(input())

while (t !=0):
    
    
    students = []
    records = []

    for i in range(t):
        students.append(input())
    
    for i in range(t*2-1):
        idx,ab = map(str,input().split())
        records.append(int(idx))
    
    for i in range(t):
        if records.count(i+1) == 1:
            ans.append(students[i])
    
    t = int(input())

for i in range(len(ans)):
    print(str(i+1) + " " + ans[i])