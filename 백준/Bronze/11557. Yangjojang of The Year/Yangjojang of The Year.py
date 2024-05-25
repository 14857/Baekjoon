t = int(input())

for _ in range(t):
    lst = []
    
    n = int(input())
    
    for i in range(n):
        school, L = input().split()
        lst.append([school,int(L)])
    
    lst.sort(key = lambda x :(x[1],x[0]))
    print(lst[-1][0])