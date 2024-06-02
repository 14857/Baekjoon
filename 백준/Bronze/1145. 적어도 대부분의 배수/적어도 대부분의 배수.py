# 서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램

n = list(map(int,input().split()))

for i in range(min(n),1000001):
    count = 0
    if i % n[0] == 0:
        count += 1
    
    if i % n[1] == 0:
        count += 1
        
    if i % n[2] == 0:
        count += 1
        
    if i % n[3] == 0:
        count += 1
        
    if i % n[4] == 0:
        count += 1
        
    if count >= 3:
        print(i)
        break