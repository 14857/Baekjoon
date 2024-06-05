# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열
# queue 이용

def josephus(queue, k):
    result = []
    num = k-1 # 리스트 인덱스
    
    for i in range(len(queue)):
        
        if (len(queue) > num): # 남은 사람들이 num보다 큰 경우
            result.append(queue.pop(num)) # 해당되는 수는 result로
            num += k-1
            
        else: # 남은 사람들이 num보다 작은 경우
            num = num % len(queue)
            result.append(queue.pop(num))
            num += k-1
            
    return result

# main
n,k = map(int,input().split())
queue = [i for i in range(1,n+1)]

result = josephus(queue,k)

# 출력7 
ans = str(result[0])

for i in result[1:]:
    ans += ", " + str(i)

print('<'+ ans +'>')
