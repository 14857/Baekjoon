import sys

lst = [0] *10001

n = int(sys.stdin.readline())

for i in range(n): 
    lst[int(sys.stdin.readline())] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)
            