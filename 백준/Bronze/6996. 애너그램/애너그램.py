t = int(input())

for _ in range(t):
    a,b = map(str,input().split())

    if len(a) == len(b):
        ans = ans = a + " & " + b +" are anagrams."
        for i in a:
            if a.count(i) != b.count(i):
                ans = a + " & " + b +" are NOT anagrams."
                break
    else:
        ans = a + " & " + b +" are NOT anagrams."
        
    
    print(ans)
            
            