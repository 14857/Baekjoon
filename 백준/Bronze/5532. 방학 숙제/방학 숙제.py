L = int(input())

A = int(input())
B = int(input())

C = int(input())
D = int(input())

if A%C != 0:
    ans1 = A//C+1

else:
    ans1 = A//C

if B%D != 0:
    ans2 = B//D+1

else:
    ans2 = B//D

print(L-max(ans1,ans2))