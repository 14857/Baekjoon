ans = 0
v = ['a','e','i','o','u']
s = input()

for i in s:
    if i in v:
        ans += 1
    
print(ans)