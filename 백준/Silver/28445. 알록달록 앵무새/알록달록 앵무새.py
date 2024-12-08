# 자식 앵무새의 몸통 색은 아빠 새의 몸통 색과 꼬리 색, 엄마 새의 몸통 색과 꼬리 색 중 하나이며
# 꼬리 색도 마찬가지로 이 넷 중 하나의 색으로 정해진다
# 능한 자식 앵무새의 몸통 색과 꼬리색의 모든 쌍을 사전 순으로 출력
# 중복되는 몸통 색, 꼬리 색의 쌍은 출력하지 않는다

color = []
color += list(map(str ,input().split()))
color += list(map(str ,input().split()))

color = set(color)
color = list(color)
color.sort()

for i in (color):
    for j in (color):
        print(i,j)