# 영어 알파벳을 13글자씩 밀어서 나타내기 -> 아스키코드 사용

s = input()

for i in s:
    if i.islower(): #소문자인 경우 (97~122)
        print(chr(97 + (ord(i)+13-97)%26), end = '')        
    
    elif i.isupper(): #대문자인 경우 (65~90)
        print(chr(65 + (ord(i)+13-65)%26), end = '')
    
    else: #띄어쓰기 및 숫자 등
        print(i, end = '')
        
        