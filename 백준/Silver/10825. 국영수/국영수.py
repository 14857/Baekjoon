student = []
n = int(input())

for i in range(n):
    info = list(input().split())
    student.append(info)
    
student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
    print(i[0])
