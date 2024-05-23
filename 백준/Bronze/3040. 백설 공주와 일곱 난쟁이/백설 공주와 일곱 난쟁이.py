n = []

for _ in range(9):
    n.append(int(input()))
    
sum = sum(n)

for i in range(8):
    for j in range(i+1,9):
        if sum-(n[i]+n[j]) == 100:
            ans1 = n[i]
            ans2 = n[j]
            break

n.remove(ans1)
n.remove(ans2)

for i in n:
    print(i)