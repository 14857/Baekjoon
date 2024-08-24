def gcd(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

e = a * d + b * c
f = b * d

print(e//gcd(e, f), f//gcd(e, f))