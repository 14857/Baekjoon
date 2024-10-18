# 슬라이싱 사용 -> 시간초과 발
# 현 구간합에서 맨 앞의 원소를 빼고 맨 뒤의 원소를 더한다
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

days = list(map(int,input().split()))

ans = [sum(days[:k])]

for i in range(n-k):
    ans.append(ans[i]-days[i]+days[k+i])
    
print(max(ans))