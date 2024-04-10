# 첫째 줄에는 스위치 개수/둘째 줄에는 각 스위치의 상태/셋째 줄에는 학생수
# 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수
# 한 줄에 20개씩 출력

def check(a,b):
    if switch[a-1] == switch[b+1]: # 대칭인 경우
        #바꾸기
        if switch[a-1] ==  0:
                switch[a-1] =  1
                switch[b+1] = 1
        else:
                switch[a-1] =  0
                switch[b+1] = 0
        
        # 재귀 사용 전 확인       
        if (a-2 >= 0) and (b+2<switch_num):
            check(a-1,b+1)
            
        else:
            return 0


switch_num = int(input())
switch = list(map(int,input().split()))
student = int(input())

for i in range(student):
    s, n = map(int,input().split())
    
    if s == 1: # 남학생인 경우 -> 배수 스위치 상태 변화
        for a in range(1,(switch_num//n)+1):
            if switch[a*n-1] == 0:
                switch[a*n-1] = 1
            else:
                switch[a*n-1] = 0
        
                
    elif s == 2: # 여학생인 경우 -> 조건에 해당하는 구간 스위치 변화
        
        if switch[n-1] ==  0:
            switch[n-1] =  1
        else:
            switch[n-1] =  0
        
        if (n-1>0) and (n-1<switch_num-1):
            check(n-1,n-1)
          

for i in range(0, switch_num, 20):
    print(*switch[i:i+20])
