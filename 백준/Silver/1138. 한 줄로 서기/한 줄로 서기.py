#  자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억
# n은 사람의 수 / 자기보다 큰 사람이 왼쪽에 몇명이 있는지 list
# 줄을 선 순서대로 키를 출력

n = int(input())
nums = list(map(int,input().split()))

ans = [0]*n

for i in range(n): # 인덱스가 작은 것부터 위치 잡아주기
   count = 0
   
   for j in range(n):
        if nums[i] == count and ans[j] == 0:
            ans[j] = i+1 # 인덱스가 1부터 시작하므로
            break
        
        elif ans[j] == 0:
            count += 1
    
print(*ans)