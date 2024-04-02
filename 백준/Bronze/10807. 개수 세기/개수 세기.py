# 정수 개수 N 입력 받기
n = int(input())

# 각 정수 입력 받기
values = list(map(int,input().split()))

# 검색할 정수 입력 받기
search = int(input())

print(values.count(search))