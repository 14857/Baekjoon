# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우
# 첫째 줄에 단어의 개수 N / 둘째 줄부터 N개의 줄에 단어
# 첫째 줄에 그룹 단어의 개수를 출력

n = int(input())
ans = n


for _ in range(n):
    s = input()
    alphabet = []
    
    for i in range(len(s)):
        if (s[i] not in alphabet) or (s[i] == s[i-1] ):
            alphabet.append(s[i])
            
        
        else:
            ans -= 1
            break
print(ans)