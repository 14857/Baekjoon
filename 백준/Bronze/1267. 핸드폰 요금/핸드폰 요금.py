# 영식 요금제는 30초마다 10원씩 청구
# 민식 요금제는 60초마다 15원씩 청구

N = int(input())

time = list(map(int, input().split()))

y = m = 0

for n in time:
    y += (n//30 + 1) * 10
    m += (n//60 + 1) * 15

if m == y:
    print("Y M", m)
elif m < y:
    print("M", m)
else:
    print("Y", y)