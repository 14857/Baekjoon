import sys
input = sys.stdin.readline

n = int(input())
ans = [0]*16
ans[0] = 2

for i in range(1,n+1):
    ans[i] = ans[i-1]*2-1
    

print(ans[n]**2)