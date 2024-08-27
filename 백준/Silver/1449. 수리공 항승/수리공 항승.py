# 물이 새는 곳의 개수 N과 테이프의 길이 L (N과 L은 1,000보다 작거나 같은 자연수)
# 항승이가 필요한 테이프의 최소 개수를 구하는 프로그램

n,l = map(int,input().split())
lst = list(map(int,input().split()))

lst.sort()

start = lst[0]
count = 1

for i in lst[1:]:
    if (i+0.5) - (start-0.5) <= l:
        continue
    
    else:
        start = i
        count+=1

print(count)
