h,m,s = map(int,input().split())
time = int(input())

if time//3600 != 0:
    h += time//3600
    time = time%3600

if time//60 != 0:
    m += time//60
    time = time%60
    
s += time

if s>=60:
    s -= 60
    m += 1

if m>=60:
    m = m-60
    h += 1

if h >= 24:
    h = h%24
    
print(h,m,s)