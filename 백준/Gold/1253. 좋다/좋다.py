# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 -> “좋다(GOOD)”
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하는 프로그램
# for문 -> 시간 초과 발생
# 정렬투 포인터 사용


n = int(input())
arr = list(map(int,input().split()))

arr.sort()
ans = 0

for i in range(n):
    
    goal = arr[i]
    start = 0
    end = len(arr)-1
    
    while start < end:
        if arr[start] + arr[end] == goal: # 두 개의 합으로 나타낼 수 있는 경우
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                ans += 1
                break
        elif arr[start] + arr[end] > goal: # 두 개의 합보다 작은 경우
            end -= 1
        elif arr[start] + arr[end] < goal: # 두 개의 합보다 큰 경
            start += 1

print(ans)