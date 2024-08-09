a,b = map(int,input().split())
total = b
result = [b]

for _ in range(3):
    a,b = map(int,input().split())
    total = total-a+b
    result.append(total)

print(max(result))