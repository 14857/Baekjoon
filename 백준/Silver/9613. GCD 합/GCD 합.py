import sys
import math

n = int(input())

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    total=0
    
    for j in range(1,len(lst)):
        for k in range(j+1,len(lst)):
            total += math.gcd(lst[j],lst[k])

    print(total)
