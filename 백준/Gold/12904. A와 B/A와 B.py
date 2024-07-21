#  문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임 -> 그리디 알고리
# 문자열의 뒤에 A를 추가 / 문자열을 뒤집고 뒤에 B를 추가
# S를 T로 바꿀 수 있으면 1을 없으면 0을 출력

s = list(input())
t = list(input())

while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1] #문자열 뒤집기

if s == t:
    print(1)
else:
    print(0)
