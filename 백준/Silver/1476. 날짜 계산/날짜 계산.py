# 준규가 사는 나라에서 E S M이 우리가 알고 있는 연도로 몇 년인지 구하는 프로그램
# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

e,s,m = map(int,input().split())
 
ans = 1

while True:
    if (e-ans)%15 == 0 and (s-ans)%28==0 and (m-ans)%19==0:
        print(ans)
        break
    else:
        ans += 1