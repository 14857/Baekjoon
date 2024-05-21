# 최솟값 -> 6이 5가 될 때
# 최댓값 -> 5가 6이 될 때
a,b = map(str,input().split())

a1 = int(a.replace('6','5')) + int(b.replace('6','5'))
a2 = int(a.replace('5','6')) + int(b.replace('5','6'))

print(a1,a2)