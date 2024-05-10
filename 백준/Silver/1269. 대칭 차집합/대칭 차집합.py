a,b = map(int,input().split())
a_lst = set(map(int,input().split()))
b_lst = set(map(int,input().split()))

a1 = []
b1 = []

for i in a_lst:
    if i not in b_lst:
        a1.append(i)


for i in b_lst:
    if i not in a_lst:
        b1.append(i)

print(len(b1)+len(a1))
