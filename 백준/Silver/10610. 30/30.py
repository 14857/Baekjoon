# 30의 배수 판별  -> 10의 배수 / 3의 배수

n = list(input())

n = sorted(n, reverse = True)

sum_n = 0
for i in n:
    sum_n += int(i)


if int(n[-1]) != 0: # 10의 배수 판별
    ans = -1
else:
    if sum_n%3 != 0: # 3의 배수 판별
        ans = -1
    else:
        ans = ("".join(n))
    
print(ans)

