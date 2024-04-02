# 테스트 케이스 개수 N 입력 받기
n = int(input())

# 각 경우 별 더한 값 저장하는 리스트
sum_list = []

for i in range(n):
    a,b = map(int,input().split())
    sum_list.append(a+b)

for i in range(n):
    print(sum_list[i])