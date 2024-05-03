from itertools import combinations

n,m = map(int,input().split())
nums = list(map(int,input().split()))

card_sum = list(combinations(nums,3))


for i in range(len(card_sum)):
    card_sum[i] = sum(card_sum[i])

card_sum = set(card_sum)
card_sum = list(card_sum)

d = m - min(card_sum)
ans = 0

for i in range(0,len(card_sum)):
    if (m - card_sum[i] < d) and (card_sum[i] <= m):
        d = m - card_sum[i]
        ans = card_sum[i]
        
print(ans)