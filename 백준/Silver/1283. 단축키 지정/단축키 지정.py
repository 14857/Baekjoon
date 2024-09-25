# 총 N개의 옵션 -> 각 옵션에 단축키를 의미하는 대표 알파벳 지정
# 1. 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 이미 단축키로 지정되었는지 확인 -> 단축키로 아직 지정이 안 되어있다면 그 알파벳을 단축키로 지정
# 2. 모든 단어의 첫 글자가 이미 지정이 되어있다면 -> 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정
# 3. 어떠한 것도 단축키로 지정할 수 없다면 -> 그냥 놔두며 대소문자를 구분치 않는다.
# 옵션의 개수 N(1 ≤ N ≤ 30)

# 딕셔너리 이용해서 선정 -> 대소문자 구별 X => 대문자로 통
# replace 사용하여 바꾸기

#1순위 : 맨앞
#2순위 : 띄어쓰기 바로 뒤

n = int(input())
lst = []
ans = []

for _ in range(n):
    s = list(input())
    flag = 0
    
    if s[0].upper() not in lst:
        lst.append(s[0].upper())
        s[0] = '[' + str(s[0]) + ']'
        flag = 1
        
    
    elif (s.count(' ') > 0):
        for j in (i for i, value in enumerate(s) if value == ' '):
            if s[1 + j].upper() not in lst:
                lst.append(s[1 + j].upper())
                s[1 + j] = '[' + str(s[1 + j]) + ']'
                flag = 1
                break
    
    
    if flag == 0:
        for i in range(1,len(s)):
            if s[i].upper() not in lst and s[i] != ' ':
                lst.append(s[i].upper())
                s[i] = '[' + str(s[i]) + ']'
                break
                        
    ans.append(''.join(s))
    
for i in ans:
    print(i)