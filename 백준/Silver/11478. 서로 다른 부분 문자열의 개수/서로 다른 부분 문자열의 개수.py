# 서로 다른 부분 문자열의 개수
s = input()

a = set()

for i in range(len(s)):
    for j in range (i,len(s)):
        a.add(s[i:j+1])

print(len(a))