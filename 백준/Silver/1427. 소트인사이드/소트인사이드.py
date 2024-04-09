# 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬

n = int(input())
ans = []

for i in str(n):
    ans.append(i)

ans.sort(reverse = True)

for i in range(len(ans)):
    print(ans[i],end='')