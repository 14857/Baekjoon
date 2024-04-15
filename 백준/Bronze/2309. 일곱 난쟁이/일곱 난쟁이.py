# 일곱 난쟁이의 키의 합이 100

lst = []
for i in range(9):
    lst.append(int(input()))

lst.sort()

for fake1 in range(len(lst)):
    for fake2 in range(fake1+1,len(lst)):
        if(sum(lst) - lst[fake1] - lst[fake2] == 100):
                       
            for i in range (len(lst)):
                if i == fake1 or i == fake2:
                    pass
                else:
                    print(lst[i])
            exit()