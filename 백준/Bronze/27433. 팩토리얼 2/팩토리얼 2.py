def fac(n):
    
    result = 1
    
    if n == 0:
        return 1
    
    result = n * fac(n-1)
    return result

num = int(input())
print(fac(num))