#문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램
num = int(input())
string = []

for _ in range(num):
    
    S = input()
    S = S[0] + S[-1]
    string.append(S)
    

for i in range(num):
    print(string[i])