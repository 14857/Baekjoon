n,m = map(int,input().split())
lst = list(map(int,input().split()))
ans = []

def back():
    if len(ans) == m:
        for i in ans:
            print(i)
    for i in lst:
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()

lst.sort()
back()