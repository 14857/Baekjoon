# 소수 판별  => 에라토스테네스의 체
import math

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

      

t = int(input())

for _ in range(t):
    n = int(input())
    
    while True:
        if is_prime(n):
            print(n)
            break
        else:
            n += 1
