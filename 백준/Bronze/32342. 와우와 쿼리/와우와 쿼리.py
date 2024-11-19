# 소리의 개수 Q (Q는 1이상 100 이하) / 분석할 소리 S

Q = int(input())

for _ in range(Q):
    S = input()
    ans = 0
    
    for i in range(len(S)-2):
        if(S[i:i+3] == "WOW"):
            ans += 1
    
    print(ans)