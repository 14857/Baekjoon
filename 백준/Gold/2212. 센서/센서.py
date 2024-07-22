# 최대 K개의 집중국의 수신 가능 영역의 길이의 합의 최솟값을 출력
# 센서 간의 거리가 먼 순서대로 정렬 + k개로 나누기(먼 거리 지우기)

n = int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수
lst = list(map(int,input().split())) # 센서의 좌표

ans = []

lst.sort()

if k>= n:
    print(0)
    exit()

for i in range(1,n):
    ans.append(lst[i] - lst[i-1])

ans.sort(reverse = True)

for _ in range(k-1):
    ans.pop(0)

print(sum(ans))
