n = int(input())
count = 0

def fac(n):
    ans = 1

    for i in range(1,n+1):
        ans = ans*i

    return str(ans)

s = fac(n)

for i in range (len(s)-1,0,-1):
    if s[i] == '0':
        count += 1
    else:
        break

print(count)