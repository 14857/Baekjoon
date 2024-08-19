# P는 선수의 수, 최대 50인 자연수
# W와 H는 100보다 작거나 같은 자연수, H는 짝수
# X와 Y는 절댓값이 100보다 작거나 같은 정수

# 링크 안에 있는 선수의 수를 출력

W, H, X, Y, P = map(int,input().split())
count = 0

for _ in range(P):
    newx, newy = map(int,input().split())
    
    if X <= newx <= X+W  and Y <= newy <= Y+H:
        count += 1
    elif (newx-X)**2 + (newy-Y-H/2)**2 <= (H/2)**2:    
        count += 1
    
    elif (newx-X-W)**2 + (newy-Y-H/2)**2 <= (H/2)**2:    
        count += 1
    
print(count)