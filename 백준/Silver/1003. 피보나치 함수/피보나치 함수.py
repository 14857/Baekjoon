# 피보나치 함수
# 각 테스트 케이스마다 0 출력 횟수, 1 출력 횟수를 공백으로 구분해서 출력
# 다이나믹 프로그래밍 -> 보텀업 방식

lst = [0]*41

lst[0] = [1,0]
lst[1] = [0,1]

t = int(input())

for i in range(2,41):
     a = lst[i-1][0] + lst[i-2][0]
     b = lst[i-1][1] + lst[i-2][1]
     lst[i] = [a,b]
     
for _ in range(t):
    n = int(input())
    print(*lst[n])