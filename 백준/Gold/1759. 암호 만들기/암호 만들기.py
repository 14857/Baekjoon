# 암호는 서로 다른 L개의 알파벳 소문자들로 구성
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측

def dfs(start):
    
    count_v = 0
    count_c = 0
    
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count_v += 1
        else:
            count_c += 1
            
    
    if len(s) == l and count_v >= 1 and count_c >= 2:
        print("".join(s))
        return
    
    for i in range(start,c):
        s.append(lst[i])
        dfs(i+1)
        s.pop()
        
l,c = map(int,input().split())
lst = list(map(str,input().split()))
s = []

lst.sort()

dfs(0)
