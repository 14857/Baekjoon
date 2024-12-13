# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램
# 그리디 알고리즘, 스택 이용

N, K = map(int, input().split())
num = list(input())

k = K
stack = []

for i in range(N):
    while(k > 0 and stack and stack[-1] < num[i]):
        stack.pop()
        k-=1
    stack.append(num[i])
    
print(''.join(stack[:N-K]))