time = []
for _ in range(4):
    time.append(int(input()))

total = sum(time)

print(total//60)
print(total%60)