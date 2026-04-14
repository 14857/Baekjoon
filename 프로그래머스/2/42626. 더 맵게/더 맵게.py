import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트를 최소 힙으로 변환
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)  # 가장 작은 값 꺼내기
        second = heapq.heappop(scoville)  
        
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        
        cnt += 1
    
    return cnt