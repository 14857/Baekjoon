def solution(n, arr1, arr2):
    answer = []
    
    # 이진수 변환 및 or 연산
    for i in range(n):
        result = bin(arr1[i] | arr2[i])[2:]
        
        # 출력 처리
        if(len(result) < n):
            result = '0'* (n - len(result)) + result
        
        result = result.replace('1','#')
        result = result.replace('0',' ')
        
        answer.append(result)
    
    
    return answer