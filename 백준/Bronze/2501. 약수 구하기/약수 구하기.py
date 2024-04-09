# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력

N,K = map(int,input().split())
ans = []

for i in range(1,N+1):
    if (N%i == 0):
        ans.append(i)
    
if (len(ans)<K):
    print(0)

else:
    print(ans[K-1])