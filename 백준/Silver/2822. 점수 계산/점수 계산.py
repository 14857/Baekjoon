# 참가자의 총 점수는 가장 높은 점수 5개의 합

lst = [] # 입력 받은 수 리스트
ans = [] # 가장 높은 점수 5개
idx = [] # 각 점수의 위치

for _ in range(8):
    lst.append(int(input()))

ans = sorted(lst, reverse = True)
ans = ans[:5]

for i in ans:
    idx.append(lst.index(i)+1)

idx = sorted(idx)

print(sum(ans))
print(*idx)