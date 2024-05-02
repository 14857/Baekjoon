# 출력은 첫째 줄에 다섯 개의 숫자를 출력
# 숫자는 상근이가 계산한 참가자의 수 - 각 기사에 적혀있는 참가자의 수

L,P = map(int,input().split())
num = list(map(int,input().split()))

cal = L*P

for i in range(5):
    num[i] -= cal
    
print(*num)