# 캠핑장을 연속하는 P일 중, L일동안만 사용가능/V일짜리 휴가 시작
case = []

while True:
    L, P, V = map(int,input().split())

    if L == 0 and P == 0 and V == 0:
        break
    
    else:
        ans = L*(V//P)
        
        if V%P >= L:
            ans += L
            
        else:
            ans += (V%P)
        
        case.append(ans)

for i in range (len(case)):
    print("Case " + str(i+1) + ": " + str(case[i]))