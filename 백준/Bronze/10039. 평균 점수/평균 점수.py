#  40점 미만 -> 40점을 받게 된다

scores = []

for _ in range(5):
    score = int(input())
    
    if score<40:
        scores.append(40)
    
    else:
        scores.append(score)

print(sum(scores)//5)
