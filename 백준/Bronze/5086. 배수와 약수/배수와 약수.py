# 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를,
# 배수라면 multiple을, 둘 다 아니라면 neither를 출력
ans = []

while True:
    
    A, B = map(int,input().split())
    
    if (A == 0 and B==0):
        break
        
    else:
        if (B%A == 0):
            ans.append("factor")
        
        elif (A%B == 0):
            ans.append("multiple")
        else:
            ans.append("neither")
    
for i in range(len(ans)):
    print(ans[i])