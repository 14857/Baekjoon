count = 0

date = int(input())
car_num = list(map(int,input().split()))

for i in range(5):
    if car_num[i] == date:
        count += 1

print(count)