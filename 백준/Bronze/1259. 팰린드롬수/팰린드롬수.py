while True:
    s = list(input())
    incorrect = 0
    
    if s == ['0']:
        break
    
    elif len(s) == 1:
        print('yes')
        
    
    else:
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                incorrect += 1
        
        if incorrect == 0:
            print('yes')
        
        else:
            print('no')
        