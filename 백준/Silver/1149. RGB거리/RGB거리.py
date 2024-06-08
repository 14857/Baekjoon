# 모든 집을 칠하는 비용의 최솟값을 출력
# 다이나믹 프로그래밍 -> 보텀업 방식

n = int(input())

lst = [] # 입력 받는 값
ans = [[0,0,0] for _ in range(n)] # dp 정보 저장 리스트
    
for _ in range(n):
    lst.append(list(map(int,input().split())))

ans[0] = lst[0]

for i in range(1,n):
   a = min(ans[i-1][2] + lst[i][0], ans[i-1][1] + lst[i][0])
   b = min(ans[i-1][2] + lst[i][1], ans[i-1][0] + lst[i][1])
   c = min(ans[i-1][1] + lst[i][2], ans[i-1][0] + lst[i][2])
   
   ans[i] = [a,b,c]
   
print(min(ans[n-1][0],ans[n-1][1], ans[n-1][2]))