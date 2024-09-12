#  테스트 케이스의 개수 T / 주사위를 두 번 던져 나온 두 수를 입력
# 각 테스트 케이스마다 "Case x: "를 출력한 다음, 주사위를 두 번 던져 나온 두 수의 합을 출력
#  테스트 케이스 번호(x)는 1부터 시작
t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    print("Case "+ str(i+1) + ": "+str(a+b))