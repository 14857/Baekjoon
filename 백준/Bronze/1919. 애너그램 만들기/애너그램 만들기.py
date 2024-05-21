A = [0]*26
B = [0]*26

ans = 0

a = input()
b = input()

for i in a:
    A[ord(i)-97] += 1
        
for i in b:
    B[ord(i)-97] += 1
 

for i in range(26):
    ans += abs(A[i]-B[i])

print(ans)