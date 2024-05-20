# 받은 점수의 합을 최대한 100에 가깝게 만든다.
# R버섯의 점수가 주어졌을 때, 마리오가 받는 점수를 출력하는 프로그램
total = 0

nums =[]
    
for i in range(10):
    nums.append(int(input()))
    
for k in nums:
    total += k
    
    if total >= 100:
        if total - 100 > 100-total+k:
            total -= k
            break
        
print(total)