s = input()

if len(s) == 1:
    print(1)

else:
    for i in range(len(s)//2):
    
        if s[i] != s[-1-i]:
             print(0)
             break
    
    
        if i == ((len(s)//2)-1):
            print(1)
            break