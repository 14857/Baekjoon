def solution(num, k):
    answer = -1
    
    snum = str(num)
    sk = str(k)
    
    if(sk in snum):
        answer =  snum.index(sk) + 1
        
    return answer