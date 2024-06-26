# m은 입력으로 주어지는 연산의 개수 / n+1개의 집합
# 런타임 에러 (RecursionError) 발생 -> 제한

import sys
sys.setrecursionlimit(1000000) # n범위
input = sys.stdin.readline


# 같은 집합에 속하는지 확인 -> 재귀 이용
def find_parent(x):
    if lst[x] != x:
        lst[x] = find_parent(lst[x])
    return lst[x]

# 합집합
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        lst[b] = a
    else:
        lst[a] = b


n, m = map(int, input().split())
lst = [i for i in range(n + 1)] # 자기 자신을 부모로 갖는 n + 1개 집합

for _ in range(m):
    s, a, b = map(int, input().split())
    
    if s == 0: # 합집합
        union(a, b)
    
    elif s == 1: # 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산 
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
