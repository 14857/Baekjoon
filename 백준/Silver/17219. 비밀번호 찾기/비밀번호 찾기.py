# 1차 시도 list, 이중 for 문 사용 -> 시간 초과
# dict 이용

n,m = map(int,input().split())
lst = dict(input().split() for _ in range(n))

    
for _ in range(m):
    s = input()
    print(lst.get(s))
