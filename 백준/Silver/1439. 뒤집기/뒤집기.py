import sys
 
input = sys.stdin.readline
 
s = input()
 
pre_num = s[0]  # 이전 숫자를 주어진 문자열의 첫 숫자로 설정
zero = 0 # 0의 묶음 개수
one = 0  # 1의 묶음 개수
 
for i in range(1, len(s)):  # 주어진 문자열의 두 번째 수부터 탐색 시작
    if pre_num != s[i]:     # 이전 숫자와 동일하지 않다면, 묶음이 종료되었음을 의미
        if pre_num == '0':  # 이전 숫자가 0이었다면 0의 묶음 개수를,
            zero += 1
        else:               # 그렇지 않다면, 1의 묶음 개수를 1 증가
            one += 1
        pre_num = s[i]      # 이전 숫자를 현재 비교하던 수로 재설정
print(min(zero, one))       # 0과 1의 각 묶음 개수 중 작은 묶음의 개수가 최종 결과
