s = input()
ans = []
for i in range(len(s)):
    ans.append(s[i::])

ans = sorted(ans)

for i in ans:
    print(i)