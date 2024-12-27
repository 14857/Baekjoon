# 그리디 알고리즘
# 사람은 max(idx-k, 0) ~ min(idx+k+1, n) 사이에 햄버거가 있다면 먹을 수 있다

n, k = map(int, input().split())
location = list(input())
ans = 0

for i in range(n):
    if location[i] == 'P':# 사람
        for i in range(max(i-k, 0), min(i+k+1, n)): #양쪽 고려
            if location[i] == 'H':
                location[i] = 0 # 계산 처리
                ans += 1
                break
print(ans)