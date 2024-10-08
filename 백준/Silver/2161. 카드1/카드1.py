# 제일 위에 있는 카드를 바닥에 버린다.
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램

nums = int(input())
card = []
ans = []

for i in range(1, nums+1):
    card.append(i)

while (len(card) != 0):
    
    #버린 카드
    ans.append(card.pop(0))
    
    if(len(card) != 0):
        card.append(card.pop(0))

for j in ans:
    print(j, end =" ")