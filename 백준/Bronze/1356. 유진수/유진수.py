# 유진수는 어떤 수를 10진수로 표현한 뒤 그 수를 두 부분으로 나눴을 때,
# 앞부분 자리수의 곱과 뒷부분 자리수의 곱이 같을 때를 말한다.

n = input()
ans = 0

for i in range(1,len(n)):
    total1,total2 = 1,1
    a,b = n[:i],n[i:]
    
    for i in a:
        total1 *= int(i)
    
    for j in b:
        total2 *= int(j)
    
    if(total1 == total2):
        ans = 1

if ans == 0:
    print("NO")
else:
    print("YES")
    