import sys
input=sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))


lst_sort = set(lst)
lst_sort = list(lst_sort)
lst_sort = sorted(lst_sort)

dic = {}
ans = []

for i in range(len(lst_sort)):
    if lst_sort[i] not in dic:
        dic[lst_sort[i]] = i
    
for i in range(n):
    if lst[i] in dic:
        ans.append(dic[lst[i]])

print(*ans)