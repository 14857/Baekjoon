# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
num.sort()
ans = []

def dfs(start,count,arr):
    global ans
    
    if count >= m:
        if arr not in ans:
            temp = []
            
            for i in arr:
                print(i,end = " ")
                temp.append(i)
            print()
            ans.append(temp)
            return
        else:
            return
   
    for i in range(start,n):
        arr.append(num[i])
        dfs(i,count+1,arr)
        arr.remove(num[i])
    
dfs(0,0,[])