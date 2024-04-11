
grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

num = 0
total = 0

for i in range(20):
    a = list(map(str,input().split()))
    
    if a[2] != "P":
        
        index = grade_list.index(a[2])
        total += float(a[1])*score_list[index]
        num += float(a[1])
        
ans = float(total/num)
    
print(ans)