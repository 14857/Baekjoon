# i부터 j까지 k가 몇 번 등장하는지 return 

def solution(i, j, k):
    answer = 0
    
    for num in range(i,j+1):
        answer += str(num).count(str(k))
    
    return answer