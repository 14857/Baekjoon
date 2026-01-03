from itertools import product

def solution(l, r):
    answer = []
    nums = [0,5]

    for i in range (len(str(l)),len(str(r))+1):
        #num_lst = list(product(nums,repeat = i))
        num_lst = [''.join(map(str, p)) for p in product(nums, repeat=i)]
        
        #print(num_lst)
        
        for num in num_lst:
            num = int(num)
            if (l<= num and num <=r):
                answer.append(num)
                
    if (len(answer) == 0):
        answer = [-1]      
    else:
        answer = set(answer)
        answer = list(answer)
        answer.sort()
    
    
    
    return answer