t = int(input())

for _ in range (t):
    
    ans = 0
    score = 0
    
    s = input()
    
    for i in range (len(s)):
        
        if s[i] == 'O':
            ans = ans + score + 1
            score += 1
        
        else:
            score = 0
        
    print(ans)
        