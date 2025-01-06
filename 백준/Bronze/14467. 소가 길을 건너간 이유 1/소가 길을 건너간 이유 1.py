# 소가 위치를 몇 번 바꿨는지 최소를 구한다
# 딕셔너리 사용

n = int(input())
 
arr = {}
count = 0
 
for i in range(n):
    a,b = map(int, input().split())
    if a not in arr:
        arr[a] = b
    else:
        if arr[a] != b:
            count += 1
            arr[a] = b
 
print(count)