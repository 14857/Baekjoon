#유클리드 호제법
def gcd(x,y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y    

A, B = map(int, input().split())
print('1' * gcd(A, B))