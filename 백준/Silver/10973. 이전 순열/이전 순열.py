# 첫째 줄에 입력으로 주어진 순열의 이전에 오는 순열을 출력한다 -> 더 작은 순열 만들기
# 사전순으로 가장 처음에 오는 순열인 경우에는 -1을 출력

# 큰 수가 앞에 배치된 경우 바꿔준다. -> idx

idx = -1

n = int(input())
lst = list(map(int,input().split()))

for i in range(n-1,0,-1):
    if (lst[i-1] > lst[i]): # 큰 수가 더 먼저 나온 경우
        idx = i-1
        break

if idx == -1:
    print(-1)

else:
    
    for i in range(n-1,0,-1): # 위치 바꿔주기
        if lst[i] < lst[idx]: 
            lst[i], lst[idx] = lst[idx], lst[i]
            break

    ans = lst[:idx+1] + sorted(lst[idx+1:], reverse=True)

    print(*ans)