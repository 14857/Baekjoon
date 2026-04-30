# 탐욕법(Greedy) > 단속카메라
# 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return

def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x: x[1])
    print(routes)
    
    camera = -30001  # 가능한 최소값보다 작게 시작
    answer = 0
    
    for start, end in routes:
        # 현재 카메라로 커버 못하면 새로 설치
        if start > camera:
            camera = end
            answer += 1
    
    return answer