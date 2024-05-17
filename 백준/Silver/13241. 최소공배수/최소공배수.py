# 최대공약수 -> 숫자 제한
# 최소공배수 = (두 수의 곱) // (최대공약수) 사용

a,b = map(int,input().split())

if a == b:
    print(a)

else:
    for i in range(min(a,b),0,-1):
        if a%i ==0 and b%i ==0:
            gcd = i
            break
    
    ans = (a*b)//gcd
    print(ans)