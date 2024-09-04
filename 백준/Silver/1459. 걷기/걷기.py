# 세준이는 현재 (0, 0) / (X, Y)에 위치한 집으로 가려고 한다
# 방법 1 : 도로를 따라서 가로나 세로로 한 블록 움직여서 이번 사거리에서 저 사거리로 움직이는 방법
# 방법 2 : 블록을 대각선으로 가로지르는 방법

# 집의 위치 X Y / 한 블록 가는데 걸리는 시간 W / 대각선으로 한 블록을 가로지르는 시간 S
# 세준이가 집에가는데 걸리는 최소시간을 출력

# 대각선 이용횟수 -> 최소 0번 , 최대 min(x,y)번 

x,y,w,s = map(int,input().split())
ans = []

# 평행 최대
ans.append((x+y)*w)

# 대각선 최대 -> 경우 두가지
if (x+y) % 2 == 0: #대각선으로만
    ans.append(max(x,y)*s)
else: # 평행 1번 무조건
    ans.append((max(x,y)-1)*s + w)

# 평행 + 대각선
ans.append((min(x,y)*s)+ ((max(x,y) - min(x,y))*w))

print(min(ans))