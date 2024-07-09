# 첫째 줄에 배열 A의 크기 N
# 둘째 줄에는 배열 A의 원소가 0번부터 차례대로
# n<=50인 자연수, 배열의 원소 <= 1000인 자연수

n = int(input())
a = list(map(int,input().split()))

p = []
a_sort = sorted(a)

for i in range(n):
    p.append(a_sort.index(a[i]))
    a_sort[a_sort.index(a[i])] = -1 # 중복 처리

print(*p)
