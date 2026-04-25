# 동적계획법(Dynamic Programming) > 정수 삼각형
# 각 수의 누적값 이용

def solution(triangle):
    answer = 0
    cal = []
    
    for i in range(len(triangle)):
        # 시작인 경우
        if(i == 0):
            cal.append(triangle[i])
            
        else:
            tmp = triangle[i]
            for j in range(len(triangle[i])):
                if(j == 0):
                    tmp[j] += triangle[i-1][0]
                elif(j == len(triangle[i])-1):
                    tmp[j] += triangle[i-1][-1]
                else:
                    tmp[j] += max(triangle[i-1][j], triangle[i-1][j-1])
                    
            cal.append(tmp)
        
    answer = max(cal[-1])
            
    return answer