# 정수 S와 K가 주어졌을 때, 합이 S인 K개의 양의 정수를 찾는다.
# 만약 여러개일 경우 그 곱을 가능한 최대로 한다. -> 가능한 최대의 곱을 출력
# K는 20보다 작거나 같고, S는 100보다 작거나 같으며 K보다 크거나 같다.

# 정수 s와 k 입력
s, k = map(int,input().split())

# 합이 s인 k 개의 양의 정수의 합이 최대 -> 수들이 최대한 비슷하고 고르게
ans = [s//k]*(k)
extra = s%k

for i in range(k):
    if extra > 0 :
        ans[i] +=1
        extra -= 1

total = 1

for i in ans:
    total *= i

print(total)
