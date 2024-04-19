t = int(input())

for i in range(t):
    s = list(input())
    
    if len(s)%2 == 1:
            ans = "NO"
            
    else:
        for _ in range(len(s)//2):
            for j in range (len(s)-1): 
                for k in range (j+1,len(s)):
                    if s[j] == '(' and s[k] == ')':
                        del s[k]
                        del s[j]
                        break
        
        if len(s) == 0:
            ans = "YES"
        else:
            ans = "NO"
                            
    print(ans)