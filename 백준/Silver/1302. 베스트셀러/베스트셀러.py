n = int(input())
dic = {}

for _ in range(n):
    a = input()
    
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1

dic = dict(sorted(dic.items(), key = lambda x : (-x[1],x[0])))
list_keys = list(dic.keys())

print(list_keys[0])