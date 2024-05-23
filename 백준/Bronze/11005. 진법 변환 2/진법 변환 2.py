n,b = map(int,input().split())

ans = ''

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n:
    ans += str(num[n%b])
    n = n//b

print(ans[::-1])