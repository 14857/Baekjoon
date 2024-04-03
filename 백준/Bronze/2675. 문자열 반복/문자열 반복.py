#문자열 S를 입력받은 후에,
#각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성
# 테스트 케이스 개수는 T

T = int(input())
result = []

for _ in range (T):
    P = ''
    R, S = map(str,input().split())
    R = int(R)
    
    for i in range(len(S)):
      P += S[i]*R
    
    result.append(P)
    

for a in range(len(result)):
    print(result[a])
    