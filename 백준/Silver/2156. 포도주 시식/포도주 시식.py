# 첫째 줄에 최대로 마실 수 있는 포도주의 양
# dp 이용
n=int(input())
array=[0]*10000
for i in range(n):
  array[i]=int(input())

d=[0]*10000
d[0]=array[0]
d[1]=array[0]+array[1]
d[2]=max(array[2]+array[0], array[2]+array[1], d[1])
for i in range(3,n):
  d[i]=max(array[i]+d[i-2], array[i]+array[i-1]+d[i-3], d[i-1])

print(max(d))