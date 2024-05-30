n = int(input())
count = 0 # 홀수면 상근 짝수면 창영

while True:
    
    if n == 0:
        break
    
    if n > 4:
        n = n-3
        count += 1
    
    else:
        n = n-1
        count += 1


if count%2 == 0:
    print("CY")

else:
    print("SK")