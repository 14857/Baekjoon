# -100 ≤ a < b ≤ 100 -> 각 부분마다 몇 개 겹치는지 확인하기
# cnt[0] : -100
# cnt[100] : 0
# cnt[200] : 100

def solution(lines):
    answer = 0
    cnt = [0]*200
    
    for line in lines:
        for i in range(line[0],line[1]):
            cnt[i+100] += 1
    
    for i in range(len(cnt)):
        if(cnt[i] >= 2):
            print(i)
            answer += 1
    
    return answer