# 종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수
# N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램

n = int(input())
a = 666

while n != 0:
    if '666' in str(a):
        n = n-1
        
        if n == 0:
            break
    a = a+1

print(a)