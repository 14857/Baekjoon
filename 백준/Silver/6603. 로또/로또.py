import sys
from itertools import combinations

while True:
    lst = list(map(int, input().split()))
    k = lst[0]
    S = lst[1:]

    for i in combinations(S, 6):
        print(*i)
        
    if k == 0:
        exit()
    print()