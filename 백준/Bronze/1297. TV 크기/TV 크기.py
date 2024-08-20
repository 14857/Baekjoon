# TV의 대각선 길이 D, TV의 높이 비율 H, TV의 너비 비율 W
# TV의 대각선 길이와, 높이 너비의 비율이 주어졌을 때, 실제 높이와 너비의 길이를 출력하는 프로그램

d,h,w = map(int, input().split())
n = (d**2/(h**2 + w**2))**0.5

print(int(n*h), int(n*w))