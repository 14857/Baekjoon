# 시리얼 번호의 길이/모든 자리수(숫자)의 합이 작은순/ 사전순
# 람다 정렬 사용

n = int(input())
nums = []
for _ in range(n):
    s = input()
    total = 0
    for i in s:
        if i.isdigit():
            total += int(i)
    
    nums.append([s,len(s),total])
    
nums = sorted(nums, key = lambda x : (x[1],x[2],x[0]))

for i in nums:
    print(i[0])