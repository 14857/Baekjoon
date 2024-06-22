# 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램
# 가장 긴 증가하는 수열 + 가장 긴 감소하는 수열 - 1
#  LIS 문제

x = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

# dp
increase = [1 for i in range(x)] # 가장 긴 증가하는 부분 수열
decrease = [1 for i in range(x)] # 가장 긴 감소하는 부분 수열

for i in range(x):
    for j in range(i): 
        if case[i] > case[j]: # LIS
            increase[i] = max(increase[i], increase[j]+1)
            
        if reverse_case[i] > reverse_case[j]: # 반대의 경우
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(x)]

for i in range(x):
    result[i] = increase[i] + decrease[x-i-1] -1

print(max(result))