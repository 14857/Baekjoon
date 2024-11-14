#  강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)
# 블루레이를 녹화할 때, 강의의 순서가 바뀌면 안 된다
# 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 같은 크기기여야 한
# 가능한 블루레이 크기중 최소를 출력
# 투 포인터 사용

n,m = map(int,input().split())
arr = list(map(int,input().split()))

# 초기값
start = max(arr)
end = sum(arr)

while start <= end:
    
    mid = (start + end) // 2 

    total = 0
    count = 1
    
    for i in arr:
        if total + i > mid:
            count += 1
            total = 0
        total += i

    if count <= m:
        ans = mid
        end = mid - 1
    
    else:
        start = mid + 1
    
print(ans)