num = [0]*26

S = input()

for i in S:
    num[ord(i)-97]+=1

print(*num)