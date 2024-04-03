char = [-1]*26

s = input()

for i in range (len(s)):
    if char[ord(s[i])-97] == -1:
        char[ord(s[i])-97] = i

print(*char)